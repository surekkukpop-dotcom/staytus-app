import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - SKZ Edition",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown('''
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    iframe { width: 100% !important; height: 100vh !important; border: none !important; }
</style>
''', unsafe_allow_html=True)

html_code = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>STATUS AI - SKZ Edition</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background-color: #000000; color: #e7e9ea; display: flex; justify-content: center; min-height: 100vh; overflow-x: hidden; }
        .app-container { width: 100%; max-width: 480px; background-color: #000000; min-height: 100vh; border-left: 1px solid #16181c; border-right: 1px solid #16181c; display: flex; flex-direction: column; position: relative; padding-bottom: 70px; }
        .top-header { position: sticky; top: 0; background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(12px); z-index: 100; padding: 12px 16px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #16181c; }
        .app-logo { font-size: 20px; font-weight: 900; background: linear-gradient(45deg, #a855f7, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; display: flex; align-items: center; gap: 6px; }
        .header-avatar { width: 36px; height: 36px; border-radius: 50%; object-fit: cover; border: 2px solid #a855f7; cursor: pointer; background: #1f2937; }
        .stories-container { display: flex; gap: 14px; padding: 14px 16px; overflow-x: auto; border-bottom: 1px solid #16181c; background: #000; }
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; flex-shrink: 0; }
        .story-ring { width: 66px; height: 66px; border-radius: 50%; padding: 2px; background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888); display: flex; align-items: center; justify-content: center; }
        .story-avatar { width: 60px; height: 60px; border-radius: 50%; border: 2px solid #000; object-fit: cover; background: #111827; }
        .story-username { font-size: 11px; color: #94a3b8; width: 68px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 600; }
        .feed { display: flex; flex-direction: column; }
        .create-post-box { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .create-post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #a855f7; background: #111827; }
        .create-post-input-area { flex: 1; display: flex; flex-direction: column; gap: 10px; }
        .create-post-textarea { width: 100%; background: transparent; border: none; color: #f7f9f9; outline: none; font-size: 15px; resize: none; min-height: 50px; }
        .create-post-actions { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #16181c; padding-top: 10px; margin-top: 4px; }
        .post-btn { background: #a855f7; color: white; border: none; padding: 8px 18px; border-radius: 20px; font-weight: 700; cursor: pointer; font-size: 14px; }
        .attach-btn { background: #1e293b; color: #a855f7; border: 1px solid #334155; padding: 6px 14px; border-radius: 16px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 6px; }
        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #111827; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 5px; margin-bottom: 4px; flex-wrap: wrap; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 13px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.45; color: #e7e9ea; margin-bottom: 10px; white-space: pre-wrap; }
        .post-image-card { width: 100%; border-radius: 16px; margin-bottom: 10px; border: 1px solid #2f3336; object-fit: cover; max-height: 340px; background: #0a0a0a; }
        .post-actions { display: flex; justify-content: space-between; max-width: 360px; color: #71767b; font-size: 13px; margin-top: 8px; }
        .action-item { display: flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px; transition: color 0.2s; }
        .action-item:hover { color: #a855f7; }
        .action-item.liked { color: #f91880; font-weight: bold; }
        .comments-list { margin-top: 12px; border-top: 1px solid #16181c; padding-top: 10px; display: flex; flex-direction: column; gap: 10px; }
        .comment-item { display: flex; gap: 10px; background: #090d16; padding: 10px 12px; border-radius: 12px; border: 1px solid #1e293b; }
        .comment-avatar { width: 34px; height: 34px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #111827; }
        .comment-body { flex: 1; }
        .comment-author { font-weight: 700; font-size: 13px; color: #f7f9f9; }
        .comment-handle { color: #64748b; font-size: 12px; }
        .comment-text { font-size: 13px; color: #cbd5e1; margin-top: 2px; line-height: 1.35; }
        .comment-reply-btn { background: none; border: none; color: #a855f7; font-size: 12px; font-weight: 700; cursor: pointer; margin-top: 6px; display: inline-block; }
        .inline-reply-box { display: none; margin-top: 8px; gap: 8px; }
        .inline-reply-box.active { display: flex; }
        .inline-reply-input { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 16px; padding: 6px 12px; color: #fff; font-size: 12px; outline: none; }
        .inline-reply-send { background: #a855f7; color: #fff; border: none; padding: 6px 12px; border-radius: 16px; font-size: 12px; font-weight: 700; cursor: pointer; }
        .dm-layout { display: flex; height: calc(100vh - 130px); background: #000; }
        .dm-sidebar { width: 110px; border-right: 1px solid #16181c; display: flex; flex-direction: column; overflow-y: auto; background: #000; }
        .dm-member-item { padding: 12px 8px; display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; border-bottom: 1px solid #16181c; text-align: center; opacity: 0.65; transition: 0.2s; }
        .dm-member-item.active { opacity: 1; background: #111827; border-left: 3px solid #a855f7; }
        .dm-member-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 1px solid #334155; background: #1f2937; }
        .dm-member-name { font-size: 11px; font-weight: 700; color: #e2e8f0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 90px; }
        .dm-chat-area { flex: 1; display: flex; flex-direction: column; background: #000; }
        .dm-chat-header { padding: 12px 16px; border-bottom: 1px solid #16181c; display: flex; align-items: center; gap: 10px; background: #090d16; }
        .dm-chat-avatar { width: 38px; height: 38px; border-radius: 50%; object-fit: cover; }
        .dm-chat-title { font-weight: 800; font-size: 15px; color: #fff; }
        .dm-chat-status { font-size: 12px; color: #10b981; font-weight: 600; }
        .dm-chat-messages { flex: 1; padding: 16px; display: flex; flex-direction: column; gap: 12px; overflow-y: auto; background: #000; }
        .chat-bubble { max-width: 82%; padding: 10px 14px; border-radius: 18px; font-size: 14px; line-height: 1.4; word-wrap: break-word; }
        .chat-bubble.incoming { background: #1e293b; color: #f1f5f9; align-self: flex-start; border-bottom-left-radius: 4px; }
        .chat-bubble.outgoing { background: #a855f7; color: #ffffff; align-self: flex-end; border-bottom-right-radius: 4px; }
        .dm-input-bar { padding: 10px 12px; border-top: 1px solid #16181c; display: flex; gap: 8px; background: #000; }
        .dm-input { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 20px; padding: 10px 16px; color: #fff; font-size: 14px; outline: none; }
        .dm-send-btn { background: #a855f7; color: #fff; border: none; padding: 0 16px; border-radius: 20px; font-weight: 700; cursor: pointer; }
        .profile-container { display: flex; flex-direction: column; background: #000; min-height: 100vh; }
        .profile-banner { width: 100%; height: 130px; object-fit: cover; background: linear-gradient(90deg, #4c1d95, #831843); }
        .profile-header { padding: 0 16px 16px 16px; position: relative; display: flex; flex-direction: column; border-bottom: 1px solid #16181c; }
        .profile-avatar-wrapper { position: relative; width: 84px; height: 84px; margin-top: -42px; margin-bottom: 10px; }
        .profile-avatar { width: 84px; height: 84px; border-radius: 50%; border: 4px solid #000; object-fit: cover; background: #1f2937; }
        .profile-cam-btn { position: absolute; bottom: 2px; right: 2px; background: #a855f7; color: #fff; border: 2px solid #000; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.5); }
        .profile-name { font-size: 20px; font-weight: 900; color: #fff; display: flex; align-items: center; gap: 6px; }
        .profile-handle { color: #64748b; font-size: 14px; margin-bottom: 8px; }
        .profile-bio { font-size: 14px; color: #e2e8f0; line-height: 1.4; margin-bottom: 12px; }
        .profile-stats { display: flex; gap: 20px; font-size: 14px; color: #94a3b8; }
        .profile-stat-num { font-weight: 800; color: #fff; }
        .bottom-nav { position: fixed; bottom: 0; width: 100%; max-width: 480px; background: rgba(0, 0, 0, 0.94); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-top: 1px solid #16181c; display: flex; justify-content: space-around; padding: 10px 0; z-index: 1000; }
        .nav-item { color: #64748b; font-size: 12px; text-decoration: none; cursor: pointer; font-weight: 700; display: flex; flex-direction: column; align-items: center; gap: 2px; transition: 0.2s; }
        .nav-item.active { color: #a855f7; }
        .nav-icon { font-size: 18px; }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="top-header">
            <div class="app-logo">
                <span>STATUS</span>
                <span style="font-size: 10px; background: #a855f7; color: #fff; padding: 2px 6px; border-radius: 8px; font-weight: 800;">SKZ AI</span>
            </div>
            <img id="userHeaderAvatar" class="header-avatar" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" onclick="switchTab('profile')">
        </div>

        <div id="tab-feed" class="tab-content active">
            <div class="stories-container" id="storiesContainer"></div>

            <div class="create-post-box">
                <img id="userPostAvatar" class="create-post-avatar" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>">
                <div class="create-post-input-area">
                    <textarea id="postInput" class="create-post-textarea" placeholder="What's happening with SKZ today, Manager?"></textarea>
                    <div id="postImagePreview" style="display:none; position:relative; margin-bottom:8px;">
                        <img id="previewImg" style="width:100%; max-height:200px; object-fit:cover; border-radius:12px; border:1px solid #334155;">
                        <button onclick="clearPostImage()" style="position:absolute; top:6px; right:6px; background:rgba(0,0,0,0.7); color:#fff; border:none; border-radius:50%; width:24px; height:24px; cursor:pointer;">✕</button>
                    </div>
                    <div class="create-post-actions">
                        <label class="attach-btn">
                            📷 <span>Add Photo</span>
                            <input type="file" id="postImageInput" accept="image/*" style="display:none;" onchange="handlePostImageSelect(event)">
                        </label>
                        <button class="post-btn" onclick="createNewPost()">Post</button>
                    </div>
                </div>
            </div>

            <div class="feed" id="feedPosts"></div>
        </div>

        <div id="tab-dms" class="tab-content">
            <div class="dm-layout">
                <div class="dm-sidebar" id="dmSidebar"></div>
                <div class="dm-chat-area">
                    <div class="dm-chat-header" id="dmChatHeader">
                        <img id="activeDMAvatar" class="dm-chat-avatar" src="">
                        <div>
                            <div id="activeDMTitle" class="dm-chat-title">Bang Chan</div>
                            <div class="dm-chat-status">● Online (AI Active)</div>
                        </div>
                    </div>
                    <div class="dm-chat-messages" id="dmChatMessages"></div>
                    <div class="dm-input-bar">
                        <input type="text" id="dmInput" class="dm-input" placeholder="Message..." onkeypress="if(event.key==='Enter') sendDM()">
                        <button class="dm-send-btn" onclick="sendDM()">Send</button>
                    </div>
                </div>
            </div>
        </div>

        <div id="tab-profile" class="tab-content">
            <div class="profile-container">
                <div class="profile-banner"></div>
                <div class="profile-header">
                    <div class="profile-avatar-wrapper">
                        <img id="profileAvatarImg" class="profile-avatar" src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>">
                        <label class="profile-cam-btn" title="Change Avatar">
                            📷
                            <input type="file" accept="image/*" style="display:none;" onchange="handleAvatarUpload(event)">
                        </label>
                    </div>
                    <div class="profile-name">Manager Gaerwenill 👑</div>
                    <div class="profile-handle">@gaerwenill</div>
                    <div class="profile-bio">Official Stray Kids Manager 🧭 | Protecting 8 shining stars ⭐ | 3RACHA & SKZ Always!</div>
                    <div class="profile-stats">
                        <div><span class="profile-stat-num">8</span> Following</div>
                        <div><span class="profile-stat-num">10.4M</span> Followers</div>
                    </div>
                </div>
                <div style="padding:12px 16px; font-weight:800; border-bottom:1px solid #16181c; color:#a855f7;">Your Manager Activity</div>
                <div id="userProfilePosts"></div>
            </div>
        </div>

        <div class="bottom-nav">
            <div class="nav-item active" id="nav-feed" onclick="switchTab('feed')">
                <span class="nav-icon">🏠</span>
                <span>Feed</span>
            </div>
            <div class="nav-item" id="nav-dms" onclick="switchTab('dms')">
                <span class="nav-icon">💬</span>
                <span>DMs</span>
            </div>
            <div class="nav-item" id="nav-profile" onclick="switchTab('profile')">
                <span class="nav-icon">👤</span>
                <span>Profile</span>
            </div>
        </div>
    </div>

    <script>
        let myAvatarUrl = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>";
        let currentPostImgBase64 = null;

        const MEMBERS = {
            bangchan: { name: "Bang Chan", handle: "@gnabnahc", avatar: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" },
            leeknow: { name: "Lee Know", handle: "@t.leeknow", avatar: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" },
            changbin: { name: "Changbin", handle: "@jutdwae", avatar: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" },
            hyunjin: { name: "Hyunjin", handle: "@hynjinnnn", avatar: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" },
            han: { name: "Han Jisung", handle: "@_doolsetnet", avatar: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" },
            felix: { name: "Felix", handle: "@yong.lixx", avatar: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" },
            seungmin: { name: "Seungmin", handle: "@miniverse.___", avatar: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" },
            in: { name: "I.N", handle: "@i.2.n.8", avatar: "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><circle cx='50' cy='50' r='50' fill='%23a855f7'/><text x='50' y='55' font-size='24' fill='%23ffffff' text-anchor='middle'>⭐</text></svg>" }
        };

        const STORIES_DATA = [
            { id: "bangchan", title: "Bang Chan", avatar: MEMBERS.bangchan.avatar },
            { id: "felix", title: "Felix", avatar: MEMBERS.felix.avatar },
            { id: "hyunjin", title: "Hyunjin", avatar: MEMBERS.hyunjin.avatar },
            { id: "leeknow", title: "Lee Know", avatar: MEMBERS.leeknow.avatar }
        ];

        let POSTS = [
            {
                id: 1,
                author: MEMBERS.bangchan.name,
                handle: MEMBERS.bangchan.handle,
                avatar: MEMBERS.bangchan.avatar,
                text: "Late night recording session in Chan studio with 3RACHA! 🎵 Huge thanks to Manager @gaerwenill! World Tour prep at 100%! 🔥",
                likes: 482910,
                liked: false,
                comments: [
                    { author: MEMBERS.felix.name, handle: MEMBERS.felix.handle, avatar: MEMBERS.felix.avatar, text: "I brought homemade brownies for everyone! 🍪 Save one for @gaerwenill!" }
                ]
            }
        ];

        let DM_MESSAGES = {
            bangchan: [
                { sender: "incoming", text: "Hey Manager @gaerwenill! Did you see the final mix?" }
            ]
        };

        let activeDMKey = "bangchan";

        window.onload = function() {
            renderStories();
            renderFeed();
            renderDMSidebar();
            renderDMChat();
        };

        function renderStories() {
            const container = document.getElementById('storiesContainer');
            container.innerHTML = STORIES_DATA.map(s => `
                <div class="story-item">
                    <div class="story-ring"><img class="story-avatar" src="${s.avatar}"></div>
                    <div class="story-username">${s.title}</div>
                </div>
            `).join('');
        }

        function renderFeed() {
            const container = document.getElementById('feedPosts');
            container.innerHTML = POSTS.map(p => `
                <div class="post">
                    <img class="post-avatar" src="${p.avatar}">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">${p.author}</span>
                            <span class="verified-badge">☑</span>
                            <span class="post-handle">${p.handle}</span>
                        </div>
                        <div class="post-text">${p.text}</div>
                        <div class="comments-list">
                            ${p.comments.map((c, idx) => `
                                <div class="comment-item">
                                    <img class="comment-avatar" src="${c.avatar}">
                                    <div class="comment-body">
                                        <span class="comment-author">${c.author}</span>
                                        <div class="comment-text">${c.text}</div>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                </div>
            `).join('');
        }

        function createNewPost() {
            const input = document.getElementById('postInput');
            const text = input.value.trim();
            if (!text && !currentPostImgBase64) return;

            const newPost = {
                id: Date.now(),
                author: "Manager Gaerwenill 👑",
                handle: "@gaerwenill",
                avatar: myAvatarUrl,
                text: text,
                likes: 1,
                liked: true,
                comments: []
            };

            POSTS.unshift(newPost);
            input.value = '';
            renderFeed();

            triggerAIBotReplies(newPost, text);
        }

        function triggerAIBotReplies(postObj, text) {
            const txt = text.toLowerCase();
            setTimeout(() => {
                let botKey = "bangchan";
                let replyText = "Great update Manager @gaerwenill! We will do our best! ❤️";

                if (txt.includes('comeback') || txt.includes('song') || txt.includes('album')) {
                    botKey = "bangchan";
                    replyText = "The track arrangement is sounding incredible Manager! 🔥";
                } else if (txt.includes('food') || txt.includes('brownie')) {
                    botKey = "felix";
                    replyText = "I made extra cookies for you Manager @gaerwenill! 🍪";
                }

                const bot = MEMBERS[botKey] || MEMBERS.bangchan;
                postObj.comments.push({
                    author: bot.name,
                    handle: bot.handle,
                    avatar: bot.avatar,
                    text: replyText
                });
                renderFeed();
            }, 1800);
        }

        function handlePostImageSelect(e) {
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(evt) {
                currentPostImgBase64 = evt.target.result;
                document.getElementById('previewImg').src = currentPostImgBase64;
                document.getElementById('postImagePreview').style.display = 'block';
            };
            reader.readAsDataURL(file);
        }

        function clearPostImage() {
            currentPostImgBase64 = null;
            document.getElementById('postImagePreview').style.display = 'none';
            document.getElementById('postImageInput').value = '';
        }

        function handleAvatarUpload(e) {
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(evt) {
                myAvatarUrl = evt.target.result;
                document.getElementById('userHeaderAvatar').src = myAvatarUrl;
                document.getElementById('userPostAvatar').src = myAvatarUrl;
                document.getElementById('profileAvatarImg').src = myAvatarUrl;
                renderFeed();
            };
            reader.readAsDataURL(file);
        }

        function renderDMSidebar() {
            const sidebar = document.getElementById('dmSidebar');
            const keys = ["bangchan", "felix", "leeknow", "changbin", "hyunjin", "han", "seungmin", "in"];
            sidebar.innerHTML = keys.map(k => `
                <div class="dm-member-item ${k === activeDMKey ? 'active' : ''}" onclick="selectDMChat('${k}')">
                    <img class="dm-member-avatar" src="${MEMBERS[k].avatar}">
                    <div class="dm-member-name">${MEMBERS[k].name}</div>
                </div>
            `).join('');
        }

        function selectDMChat(key) {
            activeDMKey = key;
            renderDMSidebar();
            renderDMChat();
        }

        function renderDMChat() {
            const m = MEMBERS[activeDMKey] || MEMBERS.bangchan;
            document.getElementById('activeDMAvatar').src = m.avatar;
            document.getElementById('activeDMTitle').innerText = m.name;

            const msgs = DM_MESSAGES[activeDMKey] || [];
            const container = document.getElementById('dmChatMessages');
            container.innerHTML = msgs.map(msg => `
                <div class="chat-bubble ${msg.sender}">
                    ${msg.text}
                </div>
            `).join('');
            container.scrollTop = container.scrollHeight;
        }

        function sendDM() {
            const input = document.getElementById('dmInput');
            const text = input.value.trim();
            if (!text) return;

            if (!DM_MESSAGES[activeDMKey]) DM_MESSAGES[activeDMKey] = [];
            DM_MESSAGES[activeDMKey].push({ sender: 'outgoing', text: text });
            input.value = '';
            renderDMChat();

            setTimeout(() => {
                DM_MESSAGES[activeDMKey].push({
                    sender: 'incoming',
                    text: "Thank you Manager @gaerwenill! I will always trust your lead! ⭐"
                });
                renderDMChat();
            }, 1400);
        }

        function switchTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));

            document.getElementById(`tab-${tabName}`).classList.add('active');
            document.getElementById(`nav-${tabName}`).classList.add('active');
        }
    </script>
</body>
</html>'''

components.html(html_code, height=900, scrolling=True)
