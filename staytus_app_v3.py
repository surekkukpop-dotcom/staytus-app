import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - Stray Kids Edition",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    iframe { width: 100% !important; height: 100vh !important; border: none !important; }
</style>
""",
    unsafe_allow_html=True,
)

html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Status AI - SKZ Edition</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
        body { background-color: #000000; color: #e7e9ea; display: flex; justify-content: center; min-height: 100vh; overflow-x: hidden; }
        
        .app-container {
            width: 100%;
            max-width: 480px;
            background-color: #000000;
            min-height: 100vh;
            border-left: 1px solid #16181c;
            border-right: 1px solid #16181c;
            display: flex;
            flex-direction: column;
            position: relative;
            padding-bottom: 70px;
        }

        .top-header {
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(12px); z-index: 100; padding: 12px 16px;
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #16181c;
        }
        .app-logo {
            font-size: 20px; font-weight: 800;
            background: linear-gradient(45deg, #a855f7, #ec4899);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }

        .stories-container {
            display: flex; gap: 14px; padding: 12px 16px; overflow-x: auto;
            border-bottom: 1px solid #16181c; scrollbar-width: none;
        }
        .stories-container::-webkit-scrollbar { display: none; }
        
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; flex-shrink: 0; }
        .story-ring {
            width: 60px; height: 60px; border-radius: 50%; padding: 2px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
        }
        .story-avatar-text { width: 54px; height: 54px; border-radius: 50%; border: 2px solid #000; background: #202327; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px; }
        .story-username { font-size: 11px; color: #71767b; width: 64px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

        .feed { display: flex; flex-direction: column; }
        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; }
        .post-avatar-text { width: 44px; height: 44px; border-radius: 50%; background: #a855f7; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px; flex-shrink: 0; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 4px; margin-bottom: 4px; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 13px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.4; color: #e7e9ea; margin-bottom: 10px; }
        .post-actions { display: flex; justify-content: space-between; max-width: 350px; color: #71767b; font-size: 13px; }

        .bottom-nav {
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.95); backdrop-filter: blur(12px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 12px 0; z-index: 1000;
        }
        .nav-item { color: #71767b; font-size: 20px; text-decoration: none; cursor: pointer; font-weight: bold; }
        .nav-item.active { color: #f7f9f9; }

        .tab-content { display: none; }
        .tab-content.active { display: block; }

        .chat-container { padding: 16px; display: flex; flex-direction: column; gap: 12px; height: calc(100vh - 180px); overflow-y: auto; }
        .chat-bubble { max-width: 80%; padding: 12px 16px; border-radius: 18px; font-size: 15px; line-height: 1.4; }
        .chat-bubble.incoming { background: #212327; color: #e7e9ea; align-self: flex-start; border-bottom-left-radius: 4px; }
        .chat-bubble.outgoing { background: #a855f7; color: white; align-self: flex-end; border-bottom-right-radius: 4px; }
        
        .chat-input-bar { position: fixed; bottom: 60px; width: 100%; max-width: 480px; background: #000; padding: 10px 16px; display: flex; gap: 10px; border-top: 1px solid #16181c; }
        .chat-input { flex: 1; background: #202327; border: none; border-radius: 20px; padding: 10px 16px; color: white; outline: none; font-size: 14px; }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="top-header">
            <div class="app-logo">✨ Status AI</div>
            <div style="color:#a855f7; font-size: 13px; font-weight: 700;">⚡ UNLIMITED ENERGY</div>
        </div>

        <!-- TAB 1: FEED -->
        <div id="tab-feed" class="tab-content active">
            <div class="stories-container">
                <div class="story-item">
                    <div class="story-ring"><div class="story-avatar-text" style="background:#ec4899;">G</div></div>
                    <span class="story-username">@gaerwenill</span>
                </div>
                <div class="story-item">
                    <div class="story-ring"><div class="story-avatar-text">BC</div></div>
                    <span class="story-username">gnabnahc</span>
                </div>
                <div class="story-item">
                    <div class="story-ring"><div class="story-avatar-text">FL</div></div>
                    <span class="story-username">yong.lixx</span>
                </div>
                <div class="story-item">
                    <div class="story-ring"><div class="story-avatar-text">LK</div></div>
                    <span class="story-username">t.leeknow</span>
                </div>
                <div class="story-item">
                    <div class="story-ring"><div class="story-avatar-text">HJ</div></div>
                    <span class="story-username">hynjinnnn</span>
                </div>
            </div>

            <div class="feed">
                <div class="post">
                    <div class="post-avatar-text">BC</div>
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Bang Chan</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@gnabnahc · 10m</span>
                        </div>
                        <div class="post-text">Huge shoutout to our head manager @gaerwenill for organizing everything for the upcoming world tour! STAYs, get ready! 🔥❤️</div>
                        <div class="post-actions">
                            <span>💬 1,420</span>
                            <span>🔄 8,900</span>
                            <span style="color:#f91880;">❤️ 45.2K</span>
                        </div>
                    </div>
                </div>

                <div class="post">
                    <div class="post-avatar-text" style="background:#e11d48;">FL</div>
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Felix</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@yong.lixx · 30m</span>
                        </div>
                        <div class="post-text">Made a fresh batch of chocolate chip cookies for @gaerwenill and all the members! Hope everyone is having a warm day ✨🍪</div>
                        <div class="post-actions">
                            <span>💬 2,310</span>
                            <span>🔄 12.4K</span>
                            <span style="color:#f91880;">❤️ 89.1K</span>
                        </div>
                    </div>
                </div>

                <div class="post">
                    <div class="post-avatar-text" style="background:#2563eb;">DP</div>
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Dispatch Official</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@kpop_dispatch · 2h</span>
                        </div>
                        <div class="post-text">🚨 EXCLUSIVE: Stray Kids Head Manager @gaerwenill spotted arriving at JYP Center. New comeback era preparing?</div>
                        <div class="post-actions">
                            <span>💬 5,820</span>
                            <span>🔄 34.1K</span>
                            <span style="color:#f91880;">❤️ 120K</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 2: DMS -->
        <div id="tab-dms" class="tab-content">
            <div style="padding: 16px; font-weight: 800; border-bottom: 1px solid #16181c; font-size: 17px;">
                Direct Messages with Stray Kids
            </div>
            <div class="chat-container" id="chat-box">
                <div class="chat-bubble incoming">
                    <strong>Bang Chan (@gnabnahc):</strong><br>
                    Hey @gaerwenill! Thanks for checking in. We just finished the vocal recording session for track 3. Do you have a moment to review the schedule for tomorrow's photoshoot?
                </div>
            </div>
            <div class="chat-input-bar">
                <input type="text" id="dm-input" class="chat-input" placeholder="Message Bang Chan as @gaerwenill...">
                <button style="background:#a855f7; color:white; border:none; padding: 0 16px; border-radius:20px; font-weight:700; cursor:pointer;" onclick="sendDM()">Send</button>
            </div>
        </div>

        <!-- BOTTOM NAV -->
        <div class="bottom-nav">
            <a class="nav-item active" onclick="switchTab('feed', this)">🏠 Feed</a>
            <a class="nav-item" onclick="switchTab('dms', this)">💬 DMs</a>
        </div>
    </div>

    <script>
        function switchTab(tabName, el) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            el.classList.add('active');
        }
        function sendDM() {
            let input = document.getElementById('dm-input');
            if (input.value.trim() !== '') {
                let chatBox = document.getElementById('chat-box');
                chatBox.innerHTML += `<div class="chat-bubble outgoing"><strong>@gaerwenill:</strong><br>${input.value}</div>`;
                let userMsg = input.value;
                input.value = '';
                chatBox.scrollTop = chatBox.scrollHeight;

                setTimeout(() => {
                    let responses = [
                        "I got your message @gaerwenill! I will make sure the rest of the members get rest before tomorrow's practice. Thanks for taking care of us!",
                        "Thanks @gaerwenill! Really appreciate your guidance as always. See you at the studio in 20 minutes!",
                        "Sounds perfect @gaerwenill. Seungmin and Lee Know are just finishing up dinner and we'll head over."
                    ];
                    let randomResp = responses[Math.floor(Math.random() * responses.length)];
                    chatBox.innerHTML += `<div class="chat-bubble incoming"><strong>Bang Chan (@gnabnahc):</strong><br>${randomResp}</div>`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                }, 1000);
            }
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
