import asyncio

from pyrogram import Client, errors, filters, types, StopPropagation
from telethon import errors as telerror, TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest

from config import SUPPORT_CHAT
from anony import app, buttons


async def listen(cq: types.CallbackQuery, text: str, timeout: int = 120) -> str:
    try:
        await cq.message.reply_text(text)
        message = await app.listen.Message(filters.text, id=filters.user(cq.from_user.id), timeout=timeout)
        return message.text
    except asyncio.TimeoutError:
        await cq.message.reply_text("Timed out.\n\nPlease try again.", reply_markup=buttons.retry_key())
        raise StopPropagation


@app.on_callback_query(filters.regex("generate"))
async def _generate(_, cq: types.CallbackQuery):
    await cq.answer()
    await cq.message.reply_text("Please choose which session you want to generate:", reply_markup=buttons.gen_key())

@app.on_callback_query(filters.regex(r"(pyrogram|telethon)"))
async def _gen_session(_, cq: types.CallbackQuery):
    sgen = cq.data
    pyrogram = sgen == "pyrogram"
    await cq.answer()
    await cq.message.reply_text(f"Starting {sgen} session generator...")

    api_id = await listen(cq, "Please enter your <b>api id</b> to proceed:")
    try:
        api_id = int(api_id)
    except ValueError:
        return await cq.message.reply_text("The <b>api id</b> you've sent is invalid.\n\nPlease start generating session again.", reply_markup=buttons.retry_key())

    api_hash = await listen(cq, "Please enter your <b>api hash</b> to proceed:")
    if len(api_hash) < 30:
        return await cq.message.reply_text("The <b>api hash</b> you've sent is invalid.\n\nPlease start generating session again.", reply_markup=buttons.retry_key())

    phone_number = await listen(cq, "Please enter your <b>phone number</b> to proceed:")
    await cq.message.reply_text("Trying to send otp at the given number...")
    client = (
        Client(name="Anony", api_id=api_id, api_hash=api_hash, in_memory=True)
        if pyrogram
        else TelegramClient(StringSession(), api_id, api_hash)
    )
    await client.connect()

    try:
        code = (
            await client.send_code(phone_number)
            if pyrogram
            else await client.send_code_request(phone_number)
        )
        await asyncio.sleep(1)

    except errors.FloodWait as f:
        return await cq.message.reply_text(f"Failed to send code for session generation.\n\nPlease wait for {f.value} seconds and try again.", reply_markup=buttons.retry_key())
    except (errors.ApiIdInvalid, telerror.ApiIdInvalidError):
        return await cq.message.reply_text("Api id or api hash is invalid.\n\nPlease start generating session again.", reply_markup=buttons.retry_key())
    except (errors.PhoneNumberInvalid, telerror.PhoneNumberInvalidError):
        return await cq.message.reply_text("Phone number invalid.\n\nPlease start generating session again.", reply_markup=buttons.retry_key())
    except Exception as ex:
        return await cq.message.reply_text(f"Error : <code>{str(ex)}</code>")

    otp = await listen(cq, f"Please enter the otp sent to {phone_number}.\n\nIf otp is <code>12345</code>, please send it as <code>1 2 3 4 5</code>", timeout=600)
    otp = otp.replace(" ", "")
    try:
        (
            await client.sign_in(phone_number, code.phone_code_hash, otp)
            if pyrogram
            else await client.sign_in(phone_number, otp)
        )
    except (errors.PhoneCodeInvalid, telerror.PhoneCodeInvalidError):
        return await cq.message.reply_text("The otp you've sent is <b>wrong.</b>\n\nPlease start generating session again.", reply_markup=buttons.retry_key())
    except (errors.PhoneCodeExpired, telerror.PhoneCodeExpiredError):
        return await cq.message.reply_text("The otp you've sent is <b>expired</b>.\n\nPlease start generating session again.", reply_markup=buttons.retry_key())
    except (errors.SessionPasswordNeeded, telerror.SessionPasswordNeededError):
        pwd = await listen(cq, "Please enter your two step verification password to continue:")

        try:
            (
                await client.check_password(password=pwd)
                if pyrogram
                else await client.sign_in(password=pwd)
            )
        except (errors.PasswordHashInvalid, telerror.PasswordHashInvalidError):
            return await cq.message.reply_text("The password you've sent is wrong.\n\nPlease start generating session again.", reply_markup=buttons.retry_key())

    except Exception as ex:
         return await cq.message.reply_text(f"Error : <code>{str(ex)}</code>")

    try:
        txt = "Here is your {0} session\n\n<code>{1}</code>\n\nA session generator bot by <a href={2}>Fallen Association</a>\n☠ <b>Note :</b> Don't share the session with anyone."
        if pyrogram:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(sgen, string_session, SUPPORT_CHAT),
                link_preview_options=types.LinkPreviewOptions(is_disabled=True),
            )
            try:
                await client.join_chat("FallenAssociation")
            except:
                pass
        else:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(sgen, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            try:
                await client(JoinChannelRequest("@FallenAssociation"))
            except:
                pass
    except KeyError:
        pass
    try:
        await client.disconnect()
        await cq.message.reply_text(f"Successfully generated your {sgen} string session.\n\nPlease check your saved messages for getting it.\n\nA string generator bot by <a href={SUPPORT_CHAT}>Fallen Association</a>.", reply_markup=buttons.pm_key(cq.from_user.id))
    except:
        pass
