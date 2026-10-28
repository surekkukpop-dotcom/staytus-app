import streamlit as st
import json
import urllib.request
import random

st.set_page_config(
    page_title="Status AI - Stray Kids Edition",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar la interfaz estandar de Streamlit para un acabado de App Nativa Móvil
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0rem !important; max-width: 100% !important; margin: 0 auto; }
    iframe { width: 100% !important; height: 100vh !important; border: none !important; }
    body { background-color: #000000 !important; }
</style>
""", unsafe_allow_html=True)

# Motor HTML5/CSS3/JavaScript completo de Status AI
app_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Status AI - Stray Kids Edition</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; -webkit-tap-highlight-color: transparent; }
        body { background-color: #000000; color: #f7f9f9; display: flex; justify-content: center; min-height: 100vh; overflow-x: hidden; }
        
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

        /* TOP HEADER */
        .top-header {
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.90);
            backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
            z-index: 100; padding: 12px 16px;
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #16181c;
        }
        .app-logo {
            font-size: 20px; font-weight: 900;
            background: linear-gradient(135deg, #a855f7, #ec4899, #f43f5e);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 8px;
        }
        .energy-badge {
            background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.4);
            color: #c084fc; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 20px;
            display: flex; align-items: center; gap: 4px;
        }

        /* STORIES CAROUSEL */
        .stories-container {
            display: flex; gap: 14px; padding: 14px 16px; overflow-x: auto;
            border-bottom: 1px solid #16181c; scrollbar-width: none; background: #000;
        }
        .stories-container::-webkit-scrollbar { display: none; }
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 6px; cursor: pointer; flex-shrink: 0; }
        .story-ring {
            width: 66px; height: 66px; border-radius: 50%; padding: 2.5px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
            transition: transform 0.2s ease;
        }
        .story-ring:active { transform: scale(0.95); }
        .story-avatar { width: 60px; height: 60px; border-radius: 50%; border: 2px solid #000; object-fit: cover; background: #16181c; }
        .story-username { font-size: 11px; color: #71767b; width: 68px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500; }

        /* STORY MODAL VIEWER */
        .story-modal {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.96); z-index: 2000; justify-content: center; align-items: center;
        }
        .story-modal.active { display: flex; }
        .story-modal-content {
            width: 100%; max-width: 440px; height: 90vh; background: #111; border-radius: 20px;
            position: relative; display: flex; flex-direction: column; overflow: hidden; border: 1px solid #222;
        }
        .story-modal-img { width: 100%; height: 75%; object-fit: cover; }
        .story-modal-header {
            position: absolute; top: 12px; left: 12px; right: 12px; display: flex;
            align-items: center; justify-content: space-between; z-index: 10;
        }
        .story-modal-user { display: flex; align-items: center; gap: 8px; background: rgba(0,0,0,0.6); padding: 6px 14px; border-radius: 20px; backdrop-filter: blur(8px); }
        .story-modal-avatar { width: 32px; height: 32px; border-radius: 50%; object-fit: cover; }
        .story-modal-caption { padding: 18px; font-size: 15px; line-height: 1.45; color: #fff; background: #111; flex: 1; border-top: 1px solid #222; }
        .close-story-btn { background: rgba(0,0,0,0.6); border: none; color: #fff; font-size: 18px; width: 34px; height: 34px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; }

        /* FEED POSTS */
        .feed { display: flex; flex-direction: column; }
        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .post-avatar { width: 46px; height: 46px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #16181c; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 5px; margin-bottom: 4px; flex-wrap: wrap; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 14px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.45; color: #e7e9ea; margin-bottom: 12px; }
        .post-image-container { margin-bottom: 12px; border-radius: 16px; overflow: hidden; border: 1px solid #2f3336; }
        .post-image { width: 100%; max-height: 380px; object-fit: cover; display: block; }
        
        .post-actions { display: flex; justify-content: space-between; max-width: 360px; color: #71767b; font-size: 14px; margin-top: 8px; }
        .action-btn { display: flex; align-items: center; gap: 6px; cursor: pointer; transition: color 0.15s; }
        .action-btn:hover { color: #1d9bf0; }
        .action-btn.liked { color: #f91880; }

        /* COMMENTS */
        .comments-list { margin-top: 12px; display: flex; flex-direction: column; gap: 8px; border-top: 1px solid #16181c; padding-top: 10px; }
        .comment-item { background: #11141a; padding: 10px 12px; border-radius: 12px; border-left: 3px solid #a855f7; font-size: 13.5px; line-height: 1.4; }
        .comment-header { font-weight: 700; color: #f7f9f9; margin-bottom: 2px; display: flex; align-items: center; gap: 4px; }

        .comment-input-box { display: flex; gap: 8px; margin-top: 10px; }
        .comment-input { flex: 1; background: #16181c; border: 1px solid #2f3336; border-radius: 20px; padding: 8px 14px; color: #fff; font-size: 13.5px; outline: none; }
        .comment-btn { background: #a855f7; color: #fff; border: none; padding: 6px 16px; border-radius: 20px; font-weight: 700; font-size: 13px; cursor: pointer; }

        /* POST CREATOR */
        .create-post-box { padding: 16px; border-bottom: 8px solid #16181c; background: #050505; }
        .create-post-textarea { width: 100%; background: #11141a; border: 1px solid #2f3336; border-radius: 14px; padding: 12px; color: #fff; font-size: 14px; outline: none; resize: none; min-height: 70px; margin-bottom: 8px; }
        .publish-btn { background: linear-gradient(135deg, #a855f7, #ec4899); color: #fff; border: none; width: 100%; padding: 11px; border-radius: 20px; font-weight: 800; font-size: 14px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; }

        /* DMS TAB */
        .dms-container { display: flex; flex-direction: column; height: calc(100vh - 135px); }
        .dms-header { padding: 14px 16px; border-bottom: 1px solid #16181c; font-weight: 800; font-size: 17px; display: flex; align-items: center; gap: 10px; background: #000; }
        .member-selector { display: flex; gap: 10px; padding: 10px 16px; overflow-x: auto; border-bottom: 1px solid #16181c; background: #08080a; scrollbar-width: none; }
        .member-selector::-webkit-scrollbar { display: none; }
        .member-chip { padding: 7px 16px; border-radius: 20px; background: #16181c; border: 1px solid #2f3336; color: #71767b; font-size: 13px; font-weight: 600; white-space: nowrap; cursor: pointer; display: flex; align-items: center; gap: 6px; flex-shrink: 0; }
        .member-chip.active { background: #a855f7; border-color: #a855f7; color: #fff; }

        .chat-box { flex: 1; padding: 16px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; background: #000; padding-bottom: 80px; }
        .chat-bubble { max-width: 84%; padding: 12px 16px; border-radius: 18px; font-size: 14.5px; line-height: 1.45; word-wrap: break-word; }
        .chat-bubble.incoming { background: #161a22; color: #f7f9f9; align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid #222730; }
        .chat-bubble.outgoing { background: linear-gradient(135deg, #9333ea, #c026d3); color: #fff; align-self: flex-end; border-bottom-right-radius: 4px; }
        .chat-sender { font-size: 11px; font-weight: 700; color: #a855f7; margin-bottom: 3px; display: block; }

        .chat-input-bar { padding: 12px 16px; background: #08080a; border-top: 1px solid #16181c; display: flex; gap: 10px; position: fixed; bottom: 65px; width: 100%; max-width: 480px; z-index: 100; }
        .chat-input { flex: 1; background: #16181c; border: 1px solid #2f3336; border-radius: 24px; padding: 10px 18px; color: #fff; font-size: 14px; outline: none; }

        /* BOTTOM NAV */
        .bottom-nav {
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.95); backdrop-filter: blur(16px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 12px 0; z-index: 1000;
        }
        .nav-item { color: #71767b; font-size: 11px; text-decoration: none; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 3px; font-weight: 600; }
        .nav-item i { font-size: 20px; }
        .nav-item.active { color: #a855f7; }

        .tab-content { display: none; }
        .tab-content.active { display: block; }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- TOP HEADER -->
        <div class="top-header">
            <div class="app-logo"><i class="fa-solid fa-sparkles"></i> Status AI</div>
            <div class="energy-badge"><i class="fa-solid fa-bolt"></i> UNLIMITED ENERGY</div>
        </div>

        <!-- TAB 1: FEED -->
        <div id="tab-feed" class="tab-content active">
            <!-- STORIES CAROUSEL -->
            <div class="stories-container">
                <div class="story-item" onclick="openStory('Bang Chan (@gnabnahc)', 'Late night working on 3RACHA track 4 in the studio! Vibe with @gaerwenill 🎧🔥', 'https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?q=80&w=800&auto=format&fit=crop', 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=200&auto=format&fit=crop')">
                    <div class="story-ring"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=200&auto=format&fit=crop" class="story-avatar"></div>
                    <span class="story-username">gnabnahc</span>
                </div>
                <div class="story-item" onclick="openStory('Felix (@yong.lixx)', 'Fresh homemade chocolate cookies for @gaerwenill & SKZ members! 🍪✨', 'https://images.unsplash.com/photo-1558961363-fa8fdf82db35?q=80&w=800&auto=format&fit=crop', 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?q=80&w=200&auto=format&fit=crop')">
                    <div class="story-ring"><img src="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?q=80&w=200&auto=format&fit=crop" class="story-avatar"></div>
                    <span class="story-username">yong.lixx</span>
                </div>
                <div class="story-item" onclick="openStory('Lee Know (@t.leeknow)', 'Sooni and Doongi say hi to Manager @gaerwenill! 🐱', 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=800&auto=format&fit=crop', 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop')">
                    <div class="story-ring"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop" class="story-avatar"></div>
                    <span class="story-username">t.leeknow</span>
                </div>
                <div class="story-item" onclick="openStory('Hyunjin (@hynjinnnn)', 'New art canvas finished before tonight rehearsal! 🎨', 'https://images.unsplash.com/photo-1579783902614-a3fb3927b675?q=80&w=800&auto=format&fit=crop', 'https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=200&auto=format&fit=crop')">
                    <div class="story-ring"><img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=200&auto=format&fit=crop" class="story-avatar"></div>
                    <span class="story-username">hynjinnnn</span>
                </div>
            </div>

            <!-- CREATE POST -->
            <div class="create-post-box">
                <textarea id="new-post-text" class="create-post-textarea" placeholder="Post official update as Head Manager @gaerwenill..."></textarea>
                <button class="publish-btn" onclick="publishPost()"><i class="fa-solid fa-paper-plane"></i> Publish Update</button>
            </div>

            <!-- FEED POSTS LIST -->
            <div class="feed" id="feed-posts">
                <!-- POST 1 -->
                <div class="post">
                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=200&auto=format&fit=crop" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Bang Chan</span> <i class="fa-solid fa-circle-check verified-badge"></i>
                            <span class="post-handle">@gnabnahc · 12m</span>
                        </div>
                        <div class="post-text">Huge shoutout to our Head Manager @gaerwenill for organizing the entire 2026 World Tour schedule! STAYs get ready! 🔥❤️</div>
                        <div class="post-image-container">
                            <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=800&auto=format&fit=crop" class="post-image">
                        </div>
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 2,420</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 11.2K</span>
                            <span class="action-btn" onclick="toggleLike(this, 84200)"><i class="fa-regular fa-heart"></i> <span class="like-count">84.2K</span></span>
                        </div>
                        <div class="comments-list">
                            <div class="comment-item">
                                <div class="comment-header">Felix <i class="fa-solid fa-circle-check verified-badge"></i> (@yong.lixx)</div>
                                So excited!! Made special brownies for @gaerwenill today! 🍪✨
                            </div>
                        </div>
                        <div class="comment-input-box">
                            <input type="text" class="comment-input" placeholder="Reply as @gaerwenill...">
                            <button class="comment-btn" onclick="addComment(this, 'Bang Chan (@gnabnahc)')">Reply</button>
                        </div>
                    </div>
                </div>

                <!-- POST 2 -->
                <div class="post">
                    <img src="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?q=80&w=200&auto=format&fit=crop" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Felix</span> <i class="fa-solid fa-circle-check verified-badge"></i>
                            <span class="post-handle">@yong.lixx · 45m</span>
                        </div>
                        <div class="post-text">Fresh chocolate cookies ready for @gaerwenill and all the members! Hope everyone has a cozy day ☀️✨</div>
                        <div class="post-image-container">
                            <img src="https://images.unsplash.com/photo-1558961363-fa8fdf82db35?q=80&w=800&auto=format&fit=crop" class="post-image">
                        </div>
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 3,180</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 18.5K</span>
                            <span class="action-btn" onclick="toggleLike(this, 124000)"><i class="fa-regular fa-heart"></i> <span class="like-count">124K</span></span>
                        </div>
                        <div class="comment-input-box">
                            <input type="text" class="comment-input" placeholder="Reply as @gaerwenill...">
                            <button class="comment-btn" onclick="addComment(this, 'Felix (@yong.lixx)')">Reply</button>
                        </div>
                    </div>
                </div>

                <!-- POST 3 DISPATCH -->
                <div class="post">
                    <img src="https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?q=80&w=200&auto=format&fit=crop" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Dispatch Official</span> <i class="fa-solid fa-circle-check verified-badge" style="color:#e11d48;"></i>
                            <span class="post-handle">@kpop_dispatch · 2h</span>
                        </div>
                        <div class="post-text">🚨 EXCLUSIVE: Stray Kids Head Manager @gaerwenill spotted arriving at JYP Center late last night. Is a comeback imminent?</div>
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 5,820</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 34.1K</span>
                            <span class="action-btn" onclick="toggleLike(this, 198000)"><i class="fa-regular fa-heart"></i> <span class="like-count">198K</span></span>
                        </div>
                        <div class="comment-input-box">
                            <input type="text" class="comment-input" placeholder="Reply as @gaerwenill...">
                            <button class="comment-btn" onclick="addComment(this, 'Dispatch (@kpop_dispatch)')">Reply</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 2: DMS -->
        <div id="tab-dms" class="tab-content">
            <div class="dms-header">
                <i class="fa-solid fa-comments" style="color:#a855f7;"></i> Direct Messages
            </div>
            <div class="member-selector">
                <div class="member-chip active" onclick="selectMember('Bang Chan', '@gnabnahc', '🐺', 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=200&auto=format&fit=crop', 'Hey @gaerwenill! Thanks for checking in mate. We just finished vocal recording for track 3. Do you have a moment to review tomorrow photoshoot schedule?', this)">🐺 Bang Chan</div>
                <div class="member-chip" onclick="selectMember('Felix', '@yong.lixx', '🐥', 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?q=80&w=200&auto=format&fit=crop', 'Hi @gaerwenill! I brought some warm homemade brownies to the studio for you and the boys! Have you had lunch yet? ✨', this)">🐥 Felix</div>
                <div class="member-chip" onclick="selectMember('Lee Know', '@t.leeknow', '🐱', 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop', 'Manager @gaerwenill, did you order pudding for rehearsal break? Sooni and Doongi are watching you. 😏', this)">🐱 Lee Know</div>
                <div class="member-chip" onclick="selectMember('Hyunjin', '@hynjinnnn', '🥟', 'https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=200&auto=format&fit=crop', '@gaerwenill! Look at this canvas painting I just finished! Do you think STAYs will like it for the album inclusions? 🎨', this)">🥟 Hyunjin</div>
            </div>

            <div class="chat-box" id="chat-box">
                <div class="chat-bubble incoming">
                    <span class="chat-sender">Bang Chan (@gnabnahc)</span>
                    Hey @gaerwenill! Thanks for checking in mate. We just finished vocal recording for track 3. Do you have a moment to review tomorrow photoshoot schedule?
                </div>
            </div>

            <div class="chat-input-bar">
                <input type="text" id="dm-input" class="chat-input" placeholder="Message Bang Chan as @gaerwenill..." onkeypress="if(event.key==='Enter') sendDM()">
                <button class="comment-btn" style="padding:0 20px;" onclick="sendDM()"><i class="fa-solid fa-paper-plane"></i></button>
            </div>
        </div>

        <!-- BOTTOM NAV BAR -->
        <div class="bottom-nav">
            <div class="nav-item active" onclick="switchTab('feed', this)"><i class="fa-solid fa-house"></i> Feed</div>
            <div class="nav-item" onclick="switchTab('dms', this)"><i class="fa-solid fa-envelope"></i> DMs</div>
        </div>
    </div>

    <!-- STORY MODAL -->
    <div class="story-modal" id="story-modal">
        <div class="story-modal-content">
            <div class="story-modal-header">
                <div class="story-modal-user">
                    <img src="" id="story-modal-avatar" class="story-modal-avatar">
                    <span id="story-modal-author" style="font-size:13px; font-weight:700;"></span>
                </div>
                <button class="close-story-btn" onclick="closeStory()">✕</button>
            </div>
            <img src="" id="story-modal-img" class="story-modal-img">
            <div id="story-modal-caption" class="story-modal-caption"></div>
        </div>
    </div>

    <script>
        let currentMember = 'Bang Chan';
        let currentHandle = '@gnabnahc';

        function switchTab(tabName, el) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            el.classList.add('active');
        }

        function openStory(author, caption, imgUrl, avatarUrl) {
            document.getElementById('story-modal-author').innerText = author;
            document.getElementById('story-modal-caption').innerText = caption;
            document.getElementById('story-modal-img').src = imgUrl;
            document.getElementById('story-modal-avatar').src = avatarUrl;
            document.getElementById('story-modal').classList.add('active');
        }

        function closeStory() {
            document.getElementById('story-modal').classList.remove('active');
        }

        function toggleLike(el, baseCount) {
            let countSpan = el.querySelector('.like-count');
            if (el.classList.contains('liked')) {
                el.classList.remove('liked');
                el.querySelector('i').className = 'fa-regular fa-heart';
                countSpan.innerText = baseCount >= 1000 ? (baseCount/1000).toFixed(1) + 'K' : baseCount;
            } else {
                el.classList.add('liked');
                el.querySelector('i').className = 'fa-solid fa-heart';
                let newCount = baseCount + 1;
                countSpan.innerText = newCount >= 1000 ? (newCount/1000).toFixed(1) + 'K' : newCount;
            }
        }

        function publishPost() {
            let textarea = document.getElementById('new-post-text');
            let text = textarea.value.trim();
            if (text) {
                let feed = document.getElementById('feed-posts');
                let newPostHTML = `
                <div class="post">
                    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=200&auto=format&fit=crop" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Gaerwenill</span> <i class="fa-solid fa-circle-check verified-badge" style="color:#ec4899;"></i>
                            <span class="post-handle">@gaerwenill · Just now</span>
                        </div>
                        <div class="post-text">${text}</div>
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 2</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 142</span>
                            <span class="action-btn" onclick="toggleLike(this, 1250)"><i class="fa-regular fa-heart"></i> <span class="like-count">1.2K</span></span>
                        </div>
                        <div class="comments-list">
                            <div class="comment-item">
                                <div class="comment-header">Bang Chan <i class="fa-solid fa-circle-check verified-badge"></i> (@gnabnahc)</div>
                                Thank you Head Manager @gaerwenill! We will do our absolute best for STAY! 🔥❤️
                            </div>
                            <div class="comment-item">
                                <div class="comment-header">Felix <i class="fa-solid fa-circle-check verified-badge"></i> (@yong.lixx)</div>
                                Thank you @gaerwenill! Always protecting us ✨ Hugs!
                            </div>
                        </div>
                    </div>
                </div>`;
                feed.insertAdjacentHTML('afterbegin', newPostHTML);
                textarea.value = '';
            }
        }

        function addComment(btn, member) {
            let input = btn.previousElementSibling;
            let val = input.value.trim();
            if (val) {
                let list = btn.parentElement.previousElementSibling;
                list.innerHTML += `
                <div class="comment-item" style="border-left-color:#ec4899;">
                    <div class="comment-header">Gaerwenill (@gaerwenill)</div>
                    ${val}
                </div>`;
                input.value = '';
                setTimeout(() => {
                    list.innerHTML += `
                    <div class="comment-item">
                        <div class="comment-header">${member}</div>
                        Got it @gaerwenill! Thanks for taking care of everything as our Head Manager! 👍✨
                    </div>`;
                }, 1000);
            }
        }

        function selectMember(name, handle, emoji, avatar, greeting, el) {
            currentMember = name;
            currentHandle = handle;
            document.querySelectorAll('.member-chip').forEach(c => c.classList.remove('active'));
            el.classList.add('active');
            document.getElementById('dm-input').placeholder = `Message ${name} as @gaerwenill...`;
            document.getElementById('chat-box').innerHTML = `
                <div class="chat-bubble incoming">
                    <span class="chat-sender">${name} (${handle})</span>
                    ${greeting}
                </div>`;
        }

        function sendDM() {
            let input = document.getElementById('dm-input');
            let val = input.value.trim();
            if (val) {
                let box = document.getElementById('chat-box');
                box.innerHTML += `<div class="chat-bubble outgoing">${val}</div>`;
                input.value = '';
                box.scrollTop = box.scrollHeight;

                setTimeout(() => {
                    let chanResp = [
                        `Thanks @gaerwenill! I will make sure the rest of the boys get enough rest mate. Appreciate your work as Head Manager! ❤️`,
                        `Got your message @gaerwenill! Meet you in the studio in 15 minutes! Let us cook some new music! 🔥`,
                        `Thanks @gaerwenill! Always making schedule so smooth for us. STAYs are going to love this!`
                    ];
                    let felixResp = [
                        `Thank you @gaerwenill!! I saved 2 big chocolate cookies for you in the practice room fridge! 🍪✨`,
                        `Aww thanks @gaerwenill! Hope you eat well today too! Sending warm hugs! ☀️`,
                        `Got it Manager @gaerwenill! Ready for vocal warmups now! 🐥`
                    ];
                    let leeknowResp = [
                        `Okay @gaerwenill. Did you bring pudding though? Sooni is watching you. 🐱`,
                        `Got it Manager @gaerwenill. Tell Changbin to stop making noise in the dressing room. 😏`,
                        `Fine fine @gaerwenill. Back to dance practice!`
                    ];
                    let hyunjinResp = [
                        `Thank you @gaerwenill! I will wear the styling you picked for tonight show! It looks so aesthetic! 🎨✨`,
                        `Manager @gaerwenill!! Kami stole my sock again 😭 see you at the venue!`,
                        `Aww thank you @gaerwenill! See you soon!`
                    ];

                    let respList = chanResp;
                    if (currentMember === 'Felix') respList = felixResp;
                    if (currentMember === 'Lee Know') respList = leeknowResp;
                    if (currentMember === 'Hyunjin') respList = hyunjinResp;

                    let randomResp = respList[Math.floor(Math.random() * respList.length)];
                    box.innerHTML += `
                    <div class="chat-bubble incoming">
                        <span class="chat-sender">${currentMember} (${currentHandle})</span>
                        ${randomResp}
                    </div>`;
                    box.scrollTop = box.scrollHeight;
                }, 1000);
            }
        }
    </script>
</body>
</html>
"""

st.components.v1.html(app_html, height=900, scrolling=True)
