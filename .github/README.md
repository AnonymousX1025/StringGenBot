<div align="center">
  <h2>──「 String Session Generator 」──</h2>
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/AnonymousX1025/StringGenBot/master/.github/start.jpg" alt="String Session Generator" width="400">
  <p><i>Available on Telegram as <a href="https://t.me/StringFatherBot">@StringFatherBot</a></i></p>
</div>

<hr>

<details>
  <summary><b>Heroku Deployment</b></summary>
  <p>
    <a href="https://dashboard.heroku.com/new?template=https://github.com/AnonymousX1025/StringGenBot">
      Click here to deploy on Heroku
    </a>
  </p>
</details>

<details>
  <summary><b>VPS / Local Deployment</b></summary>
  <ol>
    <li>Get your <a href="https://github.com/AnonymousX1025/StringGenBot/blob/master/sample.env">Necessary Variables</a></li>
    <li>Upgrade and update:
      <pre>apt-get update && apt-get upgrade -y</pre>
    </li>
    <li>Install required packages:
      <pre>apt-get install python3-pip</pre>
    </li>
    <li>Upgrade pip:
      <pre>pip3 install -U pip</pre>
    </li>
    <li>Clone the repository:
      <pre>git clone https://github.com/AnonymousX1025/StringGenBot && cd StringGenBot</pre>
    </li>
    <li>Install requirements:
      <pre>pip3 install -U -r requirements.txt</pre>
    </li>
    <li>Fill in environment variables:
      <pre>vi sample.env</pre>
      <p>Press <code>I</code> to edit, <code>Ctrl+C</code> when done, then type <code>:wq</code> to save.</p>
    </li>
    <li>Rename the env file:
      <pre>mv sample.env .env</pre>
    </li>
    <li>Install tmux and start session:
      <pre>apt install tmux && tmux</pre>
    </li>
    <li>Run the bot:
      <pre>bash start</pre>
    </li>
    <li>Detach from tmux session:
      <pre>Ctrl+b, then d</pre>
    </li>
  </ol>
  <div align="center">
    <img src="https://raw.githubusercontent.com/AnonymousX1025/StringGenBot/master/.github/comp.jpg" alt="Demo" width="400">
  </div>
</details>
<hr>
<details>
  <summary><b>Need Help?</b></summary>
  <ul>
    <li><a href="https://t.me/DevilsHeavenMF">Support Chat</a></li>
    <li><a href="https://t.me/DevilsHeavenMF">Support Channel</a></li>
  </ul>
</details>

<details>
  <summary><b>Credits</b></summary>
  <ul>
    <li><a href="https://github.com/AnonymousX1025">Me</a></li>
    <li><a href="https://github.com/pyrogram/pyrogram">Dan</a></li>
    <li><a href="https://github.com/LonamiWebs/Telethon">Lonami</a></li>
    <li><a href="https://github.com/AnonymousX1025/StringGenBot/graphs/contributors">All Contributors</a></li>
  </ul>
</details>
