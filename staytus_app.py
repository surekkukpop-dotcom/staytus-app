import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - SKZ Edition",
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

# HTML5/CSS3/JS app con avatares e imágenes SVG/Data en vivo
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
            width: 100%; max-width: 480px; background-color: #000000; min-height: 100vh;
            border-left: 1px solid #16181c; border-right: 1px solid #16181c;
            display: flex; flex-direction: column; position: relative; padding-bottom: 70px;
        }

        .top-header {
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.90);
            backdrop-filter: blur(12px); z-index: 100; padding: 12px 16px;
            display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #16181c;
        }
        .app-logo {
            font-size: 20px; font-weight: 800;
            background: linear-gradient(45deg, #a855f7, #ec4899);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .energy-badge {
            background: rgba(168, 85, 247, 0.15); border: 1px solid #a855f7;
            color: #d8b4fe; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 12px;
        }

        .stories-container {
            display: flex; gap: 14px; padding: 14px 16px; overflow-x: auto;
            border-bottom: 1px solid #16181c; scrollbar-width: none; background: #05070a;
        }
        .stories-container::-webkit-scrollbar { display: none; }
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 6px; cursor: pointer; flex-shrink: 0; }
        .story-ring {
            width: 64px; height: 64px; border-radius: 50%; padding: 2px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
        }
        .avatar-img { width: 58px; height: 58px; border-radius: 50%; border: 2px solid #000; object-fit: cover; }
        .story-username { font-size: 11px; color: #94a3b8; width: 66px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

        .create-post-box { padding: 14px 16px; border-bottom: 1px solid #16181c; background: #000; display: flex; gap: 12px; }
        .post-textarea {
            width: 100%; background: #0f172a; border: 1px solid #1e293b; border-radius: 12px;
            padding: 10px 14px; color: white; font-size: 14px; outline: none; resize: none; min-height: 48px;
        }
        .post-btn-submit {
            background: linear-gradient(45deg, #a855f7, #ec4899);
            color: white; border: none; padding: 6px 18px; border-radius: 18px; font-weight: 700; font-size: 13px; cursor: pointer;
        }

        .feed { display: flex; flex-direction: column; }
        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .post-avatar { width: 46px; height: 46px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 4px; margin-bottom: 6px; }
        .post-author { font-weight: 700; font-size: 15px; color: #f8fafc; }
        .verified-badge { color: #38bdf8; font-size: 14px; }
        .post-handle { color: #64748b; font-size: 13px; }
        .post-text { font-size: 14.5px; line-height: 1.45; color: #e2e8f0; margin-bottom: 10px; }
        .post-image-box {
            width: 100%; height: 200px; border-radius: 14px; margin-bottom: 10px; border: 1px solid #1e293b;
            background: linear-gradient(135deg, #1e1b4b, #311042); display: flex; flex-direction: column; align-items: center; justify-content: center; color: #d8b4fe; gap: 8px; font-weight: 600; font-size: 14px;
        }
        
        .post-actions { display: flex; justify-content: space-between; max-width: 320px; color: #64748b; font-size: 13px; margin-top: 6px; }
        .action-item { display: flex; align-items: center; gap: 6px; cursor: pointer; }
        .action-item.liked { color: #ec4899; }

        .comments-list { margin-top: 10px; padding-top: 10px; border-top: 1px solid #111827; display: flex; flex-direction: column; gap: 8px; }
        .comment-item { display: flex; gap: 8px; background: #090d16; padding: 8px 12px; border-radius: 12px; border: 1px solid #1e293b; }
        .comment-avatar { width: 28px; height: 28px; border-radius: 50%; object-fit: cover; }
        .comment-body { flex: 1; font-size: 13px; }
        .comment-author { font-weight: 700; color: #f1f5f9; margin-right: 4px; }
        .comment-text { color: #cbd5e1; }

        .reply-box { display: flex; gap: 8px; margin-top: 8px; }
        .reply-input { flex: 1; background: #0f172a; border: 1px solid #1e293b; border-radius: 16px; padding: 6px 12px; color: white; font-size: 12px; outline: none; }
        .reply-btn { background: #a855f7; color: white; border: none; padding: 4px 12px; border-radius: 14px; font-weight: 700; font-size: 11px; cursor: pointer; }

        .bottom-nav {
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.92); backdrop-filter: blur(12px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 12px 0; z-index: 1000;
        }
        .nav-item { color: #64748b; font-size: 18px; text-decoration: none; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 2px; }
        .nav-item.active { color: #a855f7; }
        .nav-label { font-size: 10px; font-weight: 600; }

        .tab-content { display: none; }
        .tab-content.active { display: block; }

        .chat-header { padding: 14px 16px; border-bottom: 1px solid #16181c; display: flex; align-items: center; gap: 10px; background: #05070a; }
        .chat-container { padding: 16px; display: flex; flex-direction: column; gap: 12px; height: calc(100vh - 200px); overflow-y: auto; background: #000; }
        .chat-bubble { max-width: 82%; padding: 10px 14px; border-radius: 16px; font-size: 14px; line-height: 1.45; }
        .chat-bubble.incoming { background: #1e293b; color: #f8fafc; align-self: flex-start; border-bottom-left-radius: 2px; }
        .chat-bubble.outgoing { background: linear-gradient(135deg, #a855f7, #ec4899); color: white; align-self: flex-end; border-bottom-right-radius: 2px; }
        .chat-sender { font-size: 11px; font-weight: 700; margin-bottom: 2px; opacity: 0.8; }

        .chat-input-bar { position: fixed; bottom: 60px; width: 100%; max-width: 480px; background: #05070a; padding: 10px 16px; display: flex; gap: 8px; border-top: 1px solid #16181c; }
        .chat-input { flex: 1; background: #0f172a; border: 1px solid #1e293b; border-radius: 20px; padding: 8px 16px; color: white; outline: none; font-size: 13.5px; }

        .story-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 2000; justify-content: center; align-items: center; flex-direction: column; }
        .story-modal-content { width: 90%; max-width: 400px; padding: 20px; text-align: center; position: relative; background: #0f172a; border-radius: 20px; border: 1px solid #1e293b; }
        .story-modal-close { position: absolute; top: 10px; right: 16px; color: white; font-size: 24px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- TOP HEADER -->
        <div class="top-header">
            <div class="app-logo">✨ Status AI</div>
            <div class="energy-badge">⚡ UNLIMITED ENERGY</div>
        </div>

        <!-- TAB 1: FEED -->
        <div id="tab-feed" class="tab-content active">
            <!-- STORIES BAR -->
            <div class="stories-container">
                <div class="story-item" onclick="openStory('Gaerwenill (@gaerwenill)', 'Behind the scenes with Stray Kids today! 🧭✨')">
                    <div class="story-ring"><img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23ec4899'/><text x='50%' y='55%' font-size='40' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>G</text></svg>" class="avatar-img"></div>
                    <span class="story-username">You</span>
                </div>
                <div class="story-item" onclick="openStory('Bang Chan (@gnabnahc)', 'Late night producing session at Chan\'s Room 🎧🔥')">
                    <div class="story-ring"><img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23a855f7'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>BC</text></svg>" class="avatar-img"></div>
                    <span class="story-username">gnabnahc</span>
                </div>
                <div class="story-item" onclick="openStory('Felix (@yong.lixx)', 'Freshly baked brownies for @gaerwenill & 3RACHA! 🍪✨')">
                    <div class="story-ring"><img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%2338bdf8'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>FL</text></svg>" class="avatar-img"></div>
                    <span class="story-username">yong.lixx</span>
                </div>
                <div class="story-item" onclick="openStory('Lee Know (@t.leeknowsaurus)', 'Sooni, Doongi, and Dori approve this schedule 🐱')">
                    <div class="story-ring"><img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%2322c55e'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>LK</text></svg>" class="avatar-img"></div>
                    <span class="story-username">t.leeknow</span>
                </div>
                <div class="story-item" onclick="openStory('Hyunjin (@hynjinnnn)', 'Art session finished! Drama & aesthetics 🎨')">
                    <div class="story-ring"><img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23eab308'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>HJ</text></svg>" class="avatar-img"></div>
                    <span class="story-username">hynjinnnn</span>
                </div>
                <div class="story-item" onclick="openStory('Dispatch (@kpop_dispatch)', '🚨 BREAKING: SKZ Manager spotted preparing next comeback!')">
                    <div class="story-ring"><img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23ef4444'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>DP</text></svg>" class="avatar-img"></div>
                    <span class="story-username">dispatch</span>
                </div>
            </div>

            <!-- CREATE POST INPUT -->
            <div class="create-post-box">
                <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23ec4899'/><text x='50%' y='55%' font-size='40' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>G</text></svg>" style="width:40px; height:40px; border-radius:50%;">
                <div style="flex:1; display:flex; flex-direction:column; gap:8px;">
                    <textarea id="new-post-text" class="post-textarea" placeholder="Publish update as Head Manager @gaerwenill..."></textarea>
                    <button class="post-btn-submit" onclick="publishMainPost()" style="align-self:flex-end;">Publish Post</button>
                </div>
            </div>

            <!-- FEED CONTAINER -->
            <div class="feed" id="feed-posts">
                <!-- POST 1 -->
                <div class="post">
                    <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23a855f7'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>BC</text></svg>" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Bang Chan</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@gnabnahc · 12m</span>
                        </div>
                        <div class="post-text">Huge shoutout to our head manager @gaerwenill for organizing everything for our world tour rehearsal! STAYs, get ready! 🔥❤️</div>
                        <div class="post-image-box">
                            <div>🎙️ WORLD TOUR STAGE REHEARSAL</div>
                            <div style="font-size:12px; color:#a855f7;">Stray Kids x Manager @gaerwenill</div>
                        </div>
                        <div class="post-actions">
                            <div class="action-item">💬 2,410</div>
                            <div class="action-item">🔄 14.8K</div>
                            <div class="action-item" onclick="toggleLike(this)">❤️ <span>68.2K</span></div>
                        </div>
                        <div class="comments-list">
                            <div class="comment-item">
                                <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%2338bdf8'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>FL</text></svg>" class="comment-avatar">
                                <div class="comment-body"><span class="comment-author">Felix:</span><span class="comment-text">I brought brownies to the studio @gaerwenill! 🍪✨</span></div>
                            </div>
                            <div class="comment-item">
                                <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%2322c55e'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>LK</text></svg>" class="comment-avatar">
                                <div class="comment-body"><span class="comment-author">Lee Know:</span><span class="comment-text">Great work @gaerwenill, now buy us fried chicken 🍗😏</span></div>
                            </div>
                        </div>
                        <div class="reply-box">
                            <input type="text" class="reply-input" placeholder="Comment as @gaerwenill...">
                            <button class="reply-btn" onclick="addComment(this)">Reply</button>
                        </div>
                    </div>
                </div>

                <!-- POST 2 -->
                <div class="post">
                    <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%2338bdf8'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>FL</text></svg>" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Felix</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@yong.lixx · 45m</span>
                        </div>
                        <div class="post-text">Baking day! Made chocolate chip cookies for @gaerwenill and all the members to keep our energy up! ☀️✨</div>
                        <div class="post-image-box" style="background: linear-gradient(135deg, #451a03, #78350f); color:#fef08a;">
                            <div>🍪 FRESH HOMEMADE BROWNIES</div>
                            <div style="font-size:12px;">Made for @gaerwenill & 3RACHA</div>
                        </div>
                        <div class="post-actions">
                            <div class="action-item">💬 3,890</div>
                            <div class="action-item">🔄 22.1K</div>
                            <div class="action-item" onclick="toggleLike(this)">❤️ <span>104.5K</span></div>
                        </div>
                    </div>
                </div>

                <!-- POST 3: DISPATCH -->
                <div class="post">
                    <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23ef4444'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>DP</text></svg>" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Dispatch Official</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@kpop_dispatch · 2h</span>
                        </div>
                        <div class="post-text">🚨 EXCLUSIVE: Stray Kids Head Manager @gaerwenill spotted arriving at JYP Center. New comeback era preparing?</div>
                        <div class="post-actions">
                            <div class="action-item">💬 5,820</div>
                            <div class="action-item">🔄 34.1K</div>
                            <div class="action-item" onclick="toggleLike(this)">❤️ <span>120K</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 2: DMS CHAT -->
        <div id="tab-dms" class="tab-content">
            <div class="chat-header">
                <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23a855f7'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>BC</text></svg>" style="width:36px; height:36px; border-radius:50%;">
                <div>
                    <div style="font-weight: 700; font-size: 15px;">Bang Chan (@gnabnahc) <span class="verified-badge">☑️</span></div>
                    <div style="font-size: 11px; color: #a855f7;">Active Now • SKZ Leader</div>
                </div>
            </div>
            <div class="chat-container" id="chat-box">
                <div class="chat-bubble incoming">
                    <div class="chat-sender">Bang Chan</div>
                    Hey @gaerwenill! Thanks for checking in. We just finished the vocal recording session for track 3. Do you have a moment to review the schedule for tomorrow's photoshoot?
                </div>
            </div>
            <div class="chat-input-bar">
                <input type="text" id="dm-input" class="chat-input" placeholder="Message Bang Chan as @gaerwenill...">
                <button style="background:linear-gradient(45deg, #a855f7, #ec4899); color:white; border:none; padding: 0 16px; border-radius:20px; font-weight:700; cursor:pointer;" onclick="sendDM()">Send</button>
            </div>
        </div>

        <!-- BOTTOM NAV -->
        <div class="bottom-nav">
            <a class="nav-item active" onclick="switchTab('feed', this)">
                <div>🏠</div>
                <span class="nav-label">Feed</span>
            </a>
            <a class="nav-item" onclick="switchTab('dms', this)">
                <div>💬</div>
                <span class="nav-label">DMs</span>
            </a>
        </div>
    </div>

    <!-- STORY MODAL POPUP -->
    <div id="story-modal" class="story-modal" onclick="closeStory()">
        <div class="story-modal-content" onclick="event.stopPropagation()">
            <span class="story-modal-close" onclick="closeStory()">&times;</span>
            <div id="story-title" style="font-weight:700; margin-bottom:12px; color:#f8fafc; font-size:16px;"></div>
            <div id="story-caption" style="font-size:15px; color:#cbd5e1; line-height:1.5; padding:20px 0;"></div>
        </div>
    </div>

    <script>
        function switchTab(tabName, el) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            el.classList.add('active');
        }

        function toggleLike(el) {
            if (el.classList.contains('liked')) {
                el.classList.remove('liked');
            } else {
                el.classList.add('liked');
            }
        }

        function publishMainPost() {
            let input = document.getElementById('new-post-text');
            if (input.value.trim() !== '') {
                let feed = document.getElementById('feed-posts');
                let postHTML = `
                <div class="post">
                    <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23ec4899'/><text x='50%' y='55%' font-size='40' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>G</text></svg>" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Gaerwenill</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@gaerwenill · Just now</span>
                        </div>
                        <div class="post-text">${input.value}</div>
                        <div class="post-actions">
                            <div class="action-item">💬 1</div>
                            <div class="action-item">🔄 12</div>
                            <div class="action-item" onclick="toggleLike(this)">❤️ <span>124</span></div>
                        </div>
                        <div class="comments-list">
                            <div class="comment-item">
                                <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23a855f7'/><text x='50%' y='55%' font-size='32' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>BC</text></svg>" class="comment-avatar">
                                <div class="comment-body"><span class="comment-author">Bang Chan:</span><span class="comment-text">Thank you @gaerwenill! We will work hard for STAY! ❤️</span></div>
                            </div>
                        </div>
                    </div>
                </div>`;
                feed.insertAdjacentHTML('afterbegin', postHTML);
                input.value = '';
            }
        }

        function addComment(btn) {
            let input = btn.previousElementSibling;
            if (input.value.trim() !== '') {
                let commentsList = btn.closest('.post-content').querySelector('.comments-list');
                let commentHTML = `
                <div class="comment-item">
                    <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23ec4899'/><text x='50%' y='55%' font-size='40' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>G</text></svg>" class="comment-avatar">
                    <div class="comment-body"><span class="comment-author">Gaerwenill:</span><span class="comment-text">${input.value}</span></div>
                </div>`;
                commentsList.insertAdjacentHTML('beforeend', commentHTML);
                input.value = '';
            }
        }

        function sendDM() {
            let input = document.getElementById('dm-input');
            if (input.value.trim() !== '') {
                let chatBox = document.getElementById('chat-box');
                chatBox.innerHTML += `<div class="chat-bubble outgoing"><div class="chat-sender">You (@gaerwenill)</div>${input.value}</div>`;
                let userMsg = input.value;
                input.value = '';
                chatBox.scrollTop = chatBox.scrollHeight;

                setTimeout(() => {
                    let responses = [
                        "I got your message @gaerwenill! I will make sure all members get rest before tomorrow's practice. Thanks for taking care of us!",
                        "Thanks @gaerwenill! Really appreciate your guidance as always. See you at the studio in 20 minutes!",
                        "Sounds perfect @gaerwenill. Seungmin and Lee Know are finishing dinner and then heading to rehearsal."
                    ];
                    let randomResp = responses[Math.floor(Math.random() * responses.length)];
                    chatBox.innerHTML += `<div class="chat-bubble incoming"><div class="chat-sender">Bang Chan (@gnabnahc)</div>${randomResp}</div>`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                }, 1200);
            }
        }

        function openStory(title, caption) {
            document.getElementById('story-title').innerText = title;
            document.getElementById('story-caption').innerText = caption;
            document.getElementById('story-modal').style.display = 'flex';
        }

        function closeStory() {
            document.getElementById('story-modal').style.display = 'none';
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
