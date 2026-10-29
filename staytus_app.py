import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - Stray Kids Edition",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    iframe { width: 100% !important; height: 100vh !important; border: none !important; }
</style>
""", unsafe_allow_html=True)

html_content = """<!DOCTYPE html>
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
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.88);
            backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
            z-index: 100; padding: 12px 16px;
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #16181c;
        }
        .app-logo {
            font-size: 20px; font-weight: 900;
            background: linear-gradient(45deg, #a855f7, #ec4899);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 6px;
        }
        .header-avatar {
            width: 36px; height: 36px; border-radius: 50%; object-fit: cover;
            border: 2px solid #a855f7; cursor: pointer;
        }

        /* STORIES */
        .stories-container {
            display: flex; gap: 14px; padding: 14px 16px; overflow-x: auto;
            border-bottom: 1px solid #16181c; scrollbar-width: none; background: #000000;
        }
        .stories-container::-webkit-scrollbar { display: none; }
        
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; flex-shrink: 0; }
        .story-ring {
            width: 64px; height: 64px; border-radius: 50%; padding: 2px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
        }
        .story-avatar { width: 58px; height: 58px; border-radius: 50%; border: 2px solid #000; object-fit: cover; background: #16181c; }
        .story-username { font-size: 11px; color: #71767b; width: 66px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500; }

        /* STORY MODAL */
        .story-modal {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.95); z-index: 2000; justify-content: center; align-items: center;
        }
        .story-modal.active { display: flex; }
        .story-modal-content {
            width: 100%; max-width: 440px; height: 100%; max-height: 820px;
            background: #000; position: relative; display: flex; flex-direction: column;
            border-radius: 16px; overflow: hidden;
        }
        .story-progress-bar {
            height: 3px; background: rgba(255,255,255,0.3); margin: 12px 12px 6px 12px; border-radius: 2px; overflow: hidden;
        }
        .story-progress-fill { height: 100%; background: #ffffff; width: 100%; animation: storyTimer 5s linear forwards; }
        @keyframes storyTimer { from { width: 0%; } to { width: 100%; } }

        .story-modal-header {
            display: flex; align-items: center; justify-content: space-between; padding: 6px 16px; z-index: 10;
        }
        .story-modal-user { display: flex; align-items: center; gap: 10px; }
        .story-modal-avatar { width: 38px; height: 38px; border-radius: 50%; border: 2px solid #a855f7; object-fit: cover; }
        .story-modal-title { font-weight: 700; font-size: 14px; color: #fff; }
        .story-modal-time { font-size: 12px; color: #94a3b8; }
        .story-close-btn { background: none; border: none; color: #fff; font-size: 24px; cursor: pointer; padding: 4px 8px; }

        .story-modal-body { flex: 1; display: flex; justify-content: center; align-items: center; position: relative; overflow: hidden; }
        .story-modal-img { width: 100%; height: 100%; object-fit: cover; }

        .story-modal-footer { padding: 12px 16px 20px 16px; background: rgba(0,0,0,0.8); display: flex; gap: 10px; align-items: center; }
        .story-input { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 20px; padding: 10px 16px; color: #fff; outline: none; font-size: 14px; }
        .story-send-btn { background: #a855f7; color: #fff; border: none; padding: 10px 18px; border-radius: 20px; font-weight: 700; cursor: pointer; }

        /* FEED & POSTS */
        .feed { display: flex; flex-direction: column; }
        .create-post-box { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .create-post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; border: 2px solid #a855f7; }
        .create-post-input-area { flex: 1; display: flex; flex-direction: column; gap: 10px; }
        .create-post-textarea { width: 100%; background: transparent; border: none; color: #f7f9f9; outline: none; font-size: 16px; resize: none; min-height: 50px; }
        .create-post-actions { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #16181c; padding-top: 8px; margin-top: 6px; }
        .post-btn { background: #a855f7; color: white; border: none; padding: 8px 18px; border-radius: 20px; font-weight: 700; cursor: pointer; font-size: 14px; }
        .attach-btn { background: #1e293b; color: #a855f7; border: 1px solid #334155; padding: 6px 12px; border-radius: 16px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 4px; }

        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; }
        .post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #16181c; border: 1px solid #334155; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 4px; margin-bottom: 4px; flex-wrap: wrap; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #a855f7; font-size: 13px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.4; color: #e7e9ea; margin-bottom: 10px; white-space: pre-wrap; }
        .post-image-card { width: 100%; border-radius: 16px; margin-bottom: 10px; border: 1px solid #2f3336; object-fit: cover; max-height: 340px; }

        .post-actions { display: flex; justify-content: space-between; max-width: 360px; color: #71767b; font-size: 13px; margin-top: 8px; }
        .action-item { display: flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px; transition: color 0.2s; }
        .action-item:hover { color: #a855f7; }
        .action-item.liked { color: #f91880; font-weight: bold; }

        /* COMMENTS */
        .comments-list { margin-top: 12px; border-top: 1px solid #16181c; padding-top: 10px; display: flex; flex-direction: column; gap: 10px; }
        .comment-item { display: flex; gap: 10px; background: #0b0e14; padding: 10px 12px; border-radius: 12px; border: 1px solid #1e293b; }
        .comment-avatar { width: 34px; height: 34px; border-radius: 50%; object-fit: cover; flex-shrink: 0; border: 1px solid #334155; }
        .comment-body { flex: 1; }
        .comment-author { font-weight: 700; font-size: 13px; color: #f7f9f9; }
        .comment-handle { color: #64748b; font-size: 12px; }
        .comment-text { font-size: 13px; color: #cbd5e1; margin-top: 2px; line-height: 1.3; }
        .comment-reply-btn { background: none; border: none; color: #a855f7; font-size: 12px; font-weight: 700; cursor: pointer; margin-top: 4px; display: inline-block; }
        
        .inline-reply-box { display: none; margin-top: 8px; gap: 8px; }
        .inline-reply-box.active { display: flex; }
        .inline-reply-input { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 16px; padding: 6px 12px; color: #fff; font-size: 12px; outline: none; }
        .inline-reply-send { background: #a855f7; color: #fff; border: none; padding: 6px 12px; border-radius: 16px; font-size: 12px; font-weight: 700; cursor: pointer; }

        /* DMS TAB */
        .dm-layout { display: flex; height: calc(100vh - 140px); background: #000; }
        .dm-sidebar { width: 110px; border-right: 1px solid #16181c; display: flex; flex-direction: column; overflow-y: auto; background: #000; }
        .dm-member-item { padding: 12px 8px; display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; border-bottom: 1px solid #16181c; text-align: center; opacity: 0.65; transition: 0.2s; }
        .dm-member-item.active { opacity: 1; background: #111827; border-left: 3px solid #a855f7; }
        .dm-member-avatar { width: 42px; height: 42px; border-radius: 50%; object-fit: cover; border: 1px solid #334155; }
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

        /* PROFILE TAB */
        .profile-container { display: flex; flex-direction: column; background: #000; min-height: 100vh; }
        .profile-banner { width: 100%; height: 130px; object-fit: cover; background: #1e293b; }
        .profile-header { padding: 0 16px 16px 16px; position: relative; display: flex; flex-direction: column; border-bottom: 1px solid #16181c; }
        .profile-avatar-wrapper { position: relative; width: 84px; height: 84px; margin-top: -42px; margin-bottom: 10px; }
        .profile-avatar { width: 84px; height: 84px; border-radius: 50%; border: 4px solid #000; object-fit: cover; background: #1e293b; }
        .profile-cam-btn { position: absolute; bottom: 2px; right: 2px; background: #a855f7; color: #fff; border: 2px solid #000; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.5); }
        
        .profile-name { font-size: 20px; font-weight: 900; color: #fff; display: flex; align-items: center; gap: 6px; }
        .profile-handle { color: #64748b; font-size: 14px; margin-bottom: 8px; }
        .profile-bio { font-size: 14px; color: #e2e8f0; line-height: 1.4; margin-bottom: 12px; }
        .profile-stats { display: flex; gap: 20px; font-size: 14px; color: #94a3b8; }
        .profile-stat-num { font-weight: 800; color: #fff; }

        /* BOTTOM NAV */
        .bottom-nav {
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.92); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 10px 0; z-index: 1000;
        }
        .nav-item { color: #64748b; font-size: 13px; text-decoration: none; cursor: pointer; font-weight: 700; display: flex; flex-direction: column; align-items: center; gap: 2px; transition: 0.2s; }
        .nav-item.active { color: #a855f7; }
        .nav-icon { font-size: 18px; }

        .tab-content { display: none; }
        .tab-content.active { display: block; }
    </style>
</head>
<body>

<div class="app-container">
    <!-- TOP HEADER -->
    <div class="top-header">
        <div class="app-logo">⭐ STATUS <span style="font-size:12px; background:#a855f7; color:#fff; padding:2px 6px; border-radius:8px;">SKZ</span></div>
        <img id="userHeaderAvatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ3ciIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjN2MzYWVkIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNlYzQ4OTkiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2d3KSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+nrTwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TWFuYWdlcjwvdGV4dD4KPC9zdmc+" class="header-avatar" onclick="switchTab('profileTab')">
    </div>

    <!-- STORIES BAR -->
    <div class="stories-container" id="storiesBar"></div>

    <!-- TAB 1: FEED -->
    <div id="feedTab" class="tab-content active">
        <div class="create-post-box">
            <img id="userCreatePostAvatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ3ciIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjN2MzYWVkIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNlYzQ4OTkiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2d3KSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+nrTwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TWFuYWdlcjwvdGV4dD4KPC9zdmc+" class="create-post-avatar">
            <div class="create-post-input-area">
                <textarea id="newPostText" class="create-post-textarea" placeholder="What's happening with Stray Kids? Post as @gaerwenill..."></textarea>
                <div id="postImagePreview" style="display:none; position:relative; margin-bottom:8px;">
                    <img id="postPreviewImg" src="" style="width:100%; max-height:200px; object-fit:cover; border-radius:12px;">
                    <button onclick="clearPostImage()" style="position:absolute; top:6px; right:6px; background:rgba(0,0,0,0.7); color:#fff; border:none; border-radius:50%; width:24px; height:24px; cursor:pointer;">✕</button>
                </div>
                <div class="create-post-actions">
                    <label class="attach-btn">
                        📷 Add Photo
                        <input type="file" accept="image/*" style="display:none;" onchange="handlePostImageUpload(event)">
                    </label>
                    <button class="post-btn" onclick="createNewPost()">Post</button>
                </div>
            </div>
        </div>
        <div class="feed" id="mainFeed"></div>
    </div>

    <!-- TAB 2: SEARCH / EXPLORE -->
    <div id="searchTab" class="tab-content">
        <div style="padding: 16px;">
            <input type="text" placeholder="🔍 Search STAYs, posts, trends..." style="width:100%; background:#1e293b; border:1px solid #334155; border-radius:20px; padding:12px 18px; color:#fff; font-size:14px; outline:none; margin-bottom:16px;">
            <h3 style="font-size:16px; font-weight:800; color:#fff; margin-bottom:12px;">🔥 Trending Topics</h3>
            <div style="display:flex; flex-direction:column; gap:12px;">
                <div style="background:#0b0e14; padding:12px; border-radius:12px; border:1px solid #16181c;">
                    <div style="font-size:12px; color:#64748b;">K-POP • Trending Worldwide</div>
                    <div style="font-weight:800; color:#fff; margin-top:2px;">#ManagerGaerwenill</div>
                    <div style="font-size:12px; color:#a855f7; margin-top:2px;">48.2K posts</div>
                </div>
                <div style="background:#0b0e14; padding:12px; border-radius:12px; border:1px solid #16181c;">
                    <div style="font-size:12px; color:#64748b;">Stray Kids • Trending</div>
                    <div style="font-weight:800; color:#fff; margin-top:2px;">#SKZWorldTour2026</div>
                    <div style="font-size:12px; color:#a855f7; margin-top:2px;">124.9K posts</div>
                </div>
                <div style="background:#0b0e14; padding:12px; border-radius:12px; border:1px solid #16181c;">
                    <div style="font-size:12px; color:#64748b;">Music • Trending</div>
                    <div style="font-weight:800; color:#fff; margin-top:2px;">5-STAR 10M Sales</div>
                    <div style="font-size:12px; color:#a855f7; margin-top:2px;">89.1K posts</div>
                </div>
            </div>
        </div>
    </div>

    <!-- TAB 3: DMS -->
    <div id="dmTab" class="tab-content">
        <div class="dm-layout">
            <div class="dm-sidebar" id="dmSidebar"></div>
            <div class="dm-chat-area">
                <div class="dm-chat-header" id="dmHeader">
                    <img id="activeDMAvatar" src="" class="dm-chat-avatar">
                    <div>
                        <div class="dm-chat-title" id="activeDMTitle">Bang Chan</div>
                        <div class="dm-chat-status">● Active Now</div>
                    </div>
                </div>
                <div class="dm-chat-messages" id="dmMessages"></div>
                <div class="dm-input-bar">
                    <input type="text" id="dmInput" class="dm-input" placeholder="Message..." onkeypress="if(event.key==='Enter') sendDM()">
                    <button class="dm-send-btn" onclick="sendDM()">Send</button>
                </div>
            </div>
        </div>
    </div>

    <!-- TAB 4: PROFILE -->
    <div id="profileTab" class="tab-content">
        <div class="profile-container">
            <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfNGMxZDk1IiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzRjMWQ5NSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZGIyNzc3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzRjMWQ5NSkiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfp608L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNLWiBXT1JMRCBUT1VSIDIwMjY8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIzMjAiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI2MDAiIGZvbnQtc2l6ZT0iMjAiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk9mZmljaWFsIEFubm91bmNlbWVudCDigKIgSllQIEVudGVydGFpbm1lbnQ8L3RleHQ+Cjwvc3ZnPg==" class="profile-banner">
            <div class="profile-header">
                <div class="profile-avatar-wrapper">
                    <img id="userProfileAvatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ3ciIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjN2MzYWVkIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNlYzQ4OTkiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2d3KSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+nrTwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TWFuYWdlcjwvdGV4dD4KPC9zdmc+" class="profile-avatar">
                    <label class="profile-cam-btn">
                        📷
                        <input type="file" accept="image/*" style="display:none;" onchange="handleProfilePhotoUpload(event)">
                    </label>
                </div>
                <div class="profile-name">Gaerwenill <span class="verified-badge">✔</span></div>
                <div class="profile-handle">@gaerwenill</div>
                <div class="profile-bio">🧭 Head Manager of Stray Kids @ JYP Entertainment | Protecting SKZ & STAY! 💖✨</div>
                <div class="profile-stats">
                    <div><span class="profile-stat-num">8</span> Following</div>
                    <div><span class="profile-stat-num">2.4M</span> Followers</div>
                    <div><span class="profile-stat-num">⚡ Unlimited</span> Energy</div>
                </div>
            </div>
            <div style="padding:12px 16px; font-weight:800; color:#a855f7; border-bottom:1px solid #16181c;">User Posts</div>
            <div id="userProfileFeed"></div>
        </div>
    </div>

    <!-- BOTTOM NAV -->
    <div class="bottom-nav">
        <div class="nav-item active" id="navFeed" onclick="switchTab('feedTab')">
            <span class="nav-icon">🏠</span> Feed
        </div>
        <div class="nav-item" id="navSearch" onclick="switchTab('searchTab')">
            <span class="nav-icon">🔍</span> Explore
        </div>
        <div class="nav-item" id="navDMs" onclick="switchTab('dmTab')">
            <span class="nav-icon">💬</span> DMs
        </div>
        <div class="nav-item" id="navProfile" onclick="switchTab('profileTab')">
            <span class="nav-icon">👤</span> Profile
        </div>
    </div>
</div>

<!-- STORY MODAL -->
<div class="story-modal" id="storyModal">
    <div class="story-modal-content">
        <div class="story-progress-bar"><div class="story-progress-fill" id="storyFill"></div></div>
        <div class="story-modal-header">
            <div class="story-modal-user">
                <img id="storyModalAvatar" src="" class="story-modal-avatar">
                <div>
                    <div class="story-modal-title" id="storyModalTitle">Bang Chan</div>
                    <div class="story-modal-time">2h ago</div>
                </div>
            </div>
            <button class="story-close-btn" onclick="closeStoryModal()">✕</button>
        </div>
        <div class="story-modal-body">
            <img id="storyModalImg" src="" class="story-modal-img">
        </div>
        <div class="story-modal-footer">
            <input type="text" id="storyReplyInput" class="story-input" placeholder="Reply to story...">
            <button class="story-send-btn" onclick="sendStoryReply()">Send</button>
        </div>
    </div>
</div>

<script>
    let myAvatar = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ3ciIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjN2MzYWVkIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNlYzQ4OTkiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2d3KSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+nrTwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TWFuYWdlcjwvdGV4dD4KPC9zdmc+";
    let pendingPostImg = null;

    const BOTS = {
        "bangchan": { name: "Bang Chan", handle: "@gnabnahc", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfYmMiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMWUzYThhIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMzYjgyZjYiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2JjKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+OpzwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QmFuZyBDaGFuPC90ZXh0Pgo8L3N2Zz4=", verified: true, role: "member" },
        "leeknow": { name: "Lee Know", handle: "@t.leeknowsaurus", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfbGsiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMDY1ZjQ2IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMxMGI5ODEiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2xrKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QsTwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TGVlIEtub3c8L3RleHQ+Cjwvc3ZnPg==", verified: true, role: "member" },
        "changbin": { name: "Changbin", handle: "@jutdwae", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2IiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjOTkxYjFiIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNlZjQ0NDQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2NiKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+SqjwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q2hhbmdiaW48L3RleHQ+Cjwvc3ZnPg==", verified: true, role: "member" },
        "hyunjin": { name: "Hyunjin", handle: "@hynjinnnn", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaGoiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjNTgxYzg3IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNhODU1ZjciIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2hqKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+OqDwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+SHl1bmppbjwvdGV4dD4KPC9zdmc+", verified: true, role: "member" },
        "han": { name: "Han Jisung", handle: "@_doolsetnet", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaGFuIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzg1NGQwZSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZWFiMzA4IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSIyMDAiIHJ4PSIxMDAiIGZpbGw9InVybCgjZ19oYW4pIi8+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iNzIiIHI9IjM2IiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHBhdGggZD0iTSAzMCwxNzUgQyAzMCwxMjIgMTcwLDEyMiAxNzAsMTc1IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiLz4KICA8dGV4dCB4PSIxMDAiIHk9IjkyIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjQ0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn461PC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQ2IiBmb250LWZhbWlseT0ic3lzdGVtLXVpLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjIwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5IYW48L3RleHQ+Cjwvc3ZnPg==", verified: true, role: "member" },
        "felix": { name: "Felix", handle: "@yong.lixx", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmwiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjOWEzNDEyIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmOTczMTYiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2ZsKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QpTwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RmVsaXg8L3RleHQ+Cjwvc3ZnPg==", verified: true, role: "member" },
        "seungmin": { name: "Seungmin", handle: "@miniverse.___", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc20iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMTY0ZTYzIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwNmI2ZDQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX3NtKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QtjwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U2V1bmdtaW48L3RleHQ+Cjwvc3ZnPg==", verified: true, role: "member" },
        "in": { name: "I.N", handle: "@i.2.n.8", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjODMxODQzIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNlYzQ4OTkiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX2luKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+mijwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+SS5OPC90ZXh0Pgo8L3N2Zz4=", verified: true, role: "member" },
        "dispatch": { name: "Dispatch Official", handle: "@kpop_dispatch", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZGlzcCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNiOTFjMWMiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI2RjMjYyNiIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgPC9kZWZzPgogIDxyZWN0IHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiByeD0iMTAwIiBmaWxsPSJ1cmwoI2dfZGlzcCkiLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzYiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiLz4KICA8cGF0aCBkPSJNIDMwLDE3NSBDIDMwLDEyMiAxNzAsMTIyIDE3MCwxNzUgWiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDx0ZXh0IHg9IjEwMCIgeT0iOTIiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNDQiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfmqg8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDYiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI4MDAiIGZvbnQtc2l6ZT0iMjAiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkRpc3BhdGNoPC90ZXh0Pgo8L3N2Zz4=", verified: true, role: "news" },
        "stay_world": { name: "STAY World Updates", handle: "@stay_updates", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc3RfdyIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM0YzFkOTUiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzhiNWNmNiIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgPC9kZWZzPgogIDxyZWN0IHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiByeD0iMTAwIiBmaWxsPSJ1cmwoI2dfc3RfdykiLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzYiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiLz4KICA8cGF0aCBkPSJNIDMwLDE3NSBDIDMwLDEyMiAxNzAsMTIyIDE3MCwxNzUgWiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDx0ZXh0IHg9IjEwMCIgeT0iOTIiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNDQiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfjJA8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDYiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI4MDAiIGZvbnQtc2l6ZT0iMjAiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNUQVkgTmV3czwvdGV4dD4KPC9zdmc+", verified: false, role: "stay" },
        "stay_felix": { name: "Lixxie Brownies 🍪", handle: "@felix_sunshine_stay", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc3RfZmwiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjOWEzNDEyIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmYjkyM2MiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX3N0X2ZsKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+NqjwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TGl4eGllIFNUQVk8L3RleHQ+Cjwvc3ZnPg==", verified: false, role: "stay" },
        "stay_chan": { name: "Chanie's Room Live 🎧", handle: "@chan_room_official", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc3RfY2giIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMWU0MGFmIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiM2MGE1ZmEiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX3N0X2NoKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+OpzwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0NiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q2hhbiBMaXZlPC90ZXh0Pgo8L3N2Zz4=", verified: false, role: "stay" },
        "stay_5star": { name: "SKZ 5-STAR Worldwide 🧭", handle: "@stay_forever_5star", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc3RfNXMiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjNmIyMWE4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNjMDg0ZmMiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgcng9IjEwMCIgZmlsbD0idXJsKCNnX3N0XzVzKSIvPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjcyIiByPSIzNiIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4yMiIvPgogIDxwYXRoIGQ9Ik0gMzAsMTc1IEMgMzAsMTIyIDE3MCwxMjIgMTcwLDE3NSBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjIyIi8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MiIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0NCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+4q2QPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQ2IiBmb250LWZhbWlseT0ic3lzdGVtLXVpLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjIwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj41LVNUQVIgRmFuczwvdGV4dD4KPC9zdmc+", verified: false, role: "stay" }
    };

    const BOT_RESPONSES = {
        "bangchan": [
            "Thank you @gaerwenill! We will work hard for STAY! ❤️",
            "Late night in studio... please bring iced americano @gaerwenill! ☕",
            "STAYs are going to love this update! 👍✨",
            "Chanie's Room tonight? I need to tell STAY how awesome @gaerwenill is!"
        ],
        "felix": [
            "Baked homemade brownies for @gaerwenill & the boys! 🍪",
            "Hope everyone stays warm today! ☀️❤️",
            "Deep voice practice done! Ready to shake the stage! 🔊",
            "Manager @gaerwenill is the best! Thank you for taking care of us!"
        ],
        "leeknow": [
            "Did Sooni, Doongi, and Dori approve this post @gaerwenill? 🐱",
            "Manager @gaerwenill, where is my pudding?",
            "Dancing 8 hours today. My legs are fine, my patience is not. 😏",
            "Nice post @gaerwenill. Now buy us meat. 🥩"
        ],
        "changbin": [
            "JUTDAE! We do things with conviction! 💪🔥",
            "Did you see my bicep gains in the new photoshoot @gaerwenill?!",
            "3RACHA in the house! 🎵",
            "Protein shake break over, back to recording!"
        ],
        "hyunjin": [
            "The aesthetic of this schedule is amazing @gaerwenill! 🎨✨",
            "KAMI BIT MY SOCK AGAIN 😭 @gaerwenill help me!",
            "Dramatic? Me?! I am simply expressing my artistic soul! 🎭"
        ],
        "han": [
            "I wrote 3 songs in my sleep last night! You're welcome @gaerwenill! 🎵",
            "Can we order cheesecake for lunch? For lyrical inspiration obviously.",
            "STAY!! I missed you guys so much!"
        ],
        "seungmin": [
            "Vocal practice finished! Ready for comeback @gaerwenill. 🐶",
            "@gaerwenill, Changbin hyung is being noisy during my nap.",
            "Day 1290 of teasing Changbin hyung. Going great."
        ],
        "in": [
            "Look at my OOTD for today's schedule @gaerwenill! 😎👔",
            "The hyungs bought me dinner again. Maknae wins! 🥖",
            "Maknae energy loaded! ⚡"
        ],
        "stay_world": [
            "WE LOVE YOU @gaerwenill! THANK YOU FOR PROTECTING OUR BOYS! 😭💖",
            "TRENDING #1 WORLDWIDE: #ManagerGaerwenill #StrayKidsNextEra!",
            "STAYs let's stream harder for SKZ!!"
        ],
        "stay_felix": [
            "FELIX AND MANAGER GAERWENILL INTERACTION 😭 I'M CRYING HE'S SO SWEET!",
            "Baking brownies for the team is so Felix core 🥺❤️"
        ],
        "stay_chan": [
            "CHAN CONFIRMED IT ON LIVE! Best manager ever!! 🎧🔥",
            "3RACHA is cooking up something legendary!"
        ],
        "stay_5star": [
            "STRAY KIDS EVERYWHERE ALL AROUND THE WORLD! 🧭✨",
            "10M sales milestone unlocked! SKZ paved the way!"
        ]
    };

    const STORIES = [
        { key: "bangchan", name: "Bang Chan", handle: "@gnabnahc", avatar: BOTS.bangchan.avatar, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfMWUzYThhIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzFlM2E4YSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMjU2M2ViIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzFlM2E4YSkiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfjqc8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPjNSQUNIQSBTVFVESU8gU0VTU0lPTjwvdGV4dD4KICA8dGV4dCB4PSI0MDAiIHk9IjMyMCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2UyZThmMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TGF0ZSBOaWdodCBQcm9kdWNpbmcg4oCiIE5ldyBBbGJ1bTwvdGV4dD4KPC9zdmc+", caption: "Late night producing in the studio... 🎧" },
        { key: "felix", name: "Felix", handle: "@yong.lixx", avatar: BOTS.felix.avatar, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfOWEzNDEyIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzlhMzQxMiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZWE1ODBjIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzlhMzQxMikiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfjao8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkZFTElYIEhPTUVNQURFIEJST1dOSUVTPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzIwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNjAwIiBmb250LXNpemU9IjIwIiBmaWxsPSIjZTJlOGYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5CYWtlZCB3aXRoIGxvdmUgZm9yIE1hbmFnZXIgJiBTVEFZIOKdpO+4jzwvdGV4dD4KPC9zdmc+", caption: "Fresh cookies for @gaerwenill and STAY! 🍪" },
        { key: "leeknow", name: "Lee Know", handle: "@t.leeknowsaurus", avatar: BOTS.leeknow.avatar, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfMDY1ZjQ2IiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzA2NWY0NiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDU5NjY5IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzA2NWY0NikiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLE8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNPT05JLCBET09OR0ksIERPUkk8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIzMjAiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI2MDAiIGZvbnQtc2l6ZT0iMjAiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkFwcHJvdmVkIFRvZGF5IERhbmNlIFJlaGVhcnNhbDwvdGV4dD4KPC9zdmc+", caption: "Sooni says hi! 🐱" },
        { key: "hyunjin", name: "Hyunjin", handle: "@hynjinnnn", avatar: BOTS.hyunjin.avatar, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfNTgxYzg3IiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzU4MWM4NyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjOTMzM2VhIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzU4MWM4NykiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfjqg8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkhZVU5KSU4gQVJUIENBTlZBUzwvdGV4dD4KICA8dGV4dCB4PSI0MDAiIHk9IjMyMCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2UyZThmMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+T3JpZ2luYWwgUGFpbnRpbmcgRmluaXNoZWQg4oCiIFN0dWRpbyBBZXN0aGV0aWM8L3RleHQ+Cjwvc3ZnPg==", caption: "New painting finished 🎨" },
        { key: "changbin", name: "Changbin", handle: "@jutdwae", avatar: BOTS.changbin.avatar, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfNGMxZDk1IiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzRjMWQ5NSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZGIyNzc3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzRjMWQ5NSkiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfp608L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNLWiBXT1JMRCBUT1VSIDIwMjY8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIzMjAiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI2MDAiIGZvbnQtc2l6ZT0iMjAiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk9mZmljaWFsIEFubm91bmNlbWVudCDigKIgSllQIEVudGVydGFpbm1lbnQ8L3RleHQ+Cjwvc3ZnPg==", caption: "Post-workout protein break! 💪" },
        { key: "han", name: "Han Jisung", handle: "@_doolsetnet", avatar: BOTS.han.avatar, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfMWUzYThhIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzFlM2E4YSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMjU2M2ViIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzFlM2E4YSkiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfjqc8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPjNSQUNIQSBTVFVESU8gU0VTU0lPTjwvdGV4dD4KICA8dGV4dCB4PSI0MDAiIHk9IjMyMCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2UyZThmMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TGF0ZSBOaWdodCBQcm9kdWNpbmcg4oCiIE5ldyBBbGJ1bTwvdGV4dD4KPC9zdmc+", caption: "Writing 3RACHA beat #102 🎵" },
        { key: "seungmin", name: "Seungmin", handle: "@miniverse.___", avatar: BOTS.seungmin.avatar, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfODU0ZDBlIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzg1NGQwZSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjY2E4YTA0IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzg1NGQwZSkiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfj4Y8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPjEwLDAwMCwwMDAgU0FMRVMgTUlMRVNUT05FPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzIwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNjAwIiBmb250LXNpemU9IjIwIiBmaWxsPSIjZTJlOGYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj41LVNUQVIgR2xvYmFsIFJlY29yZCDigKIgU0taIHggU1RBWTwvdGV4dD4KPC9zdmc+", caption: "Vocal warmup time 🐶" },
        { key: "in", name: "I.N", handle: "@i.2.n.8", avatar: BOTS.in.avatar, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfODMxODQzIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzgzMTg0MyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZGIyNzc3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzgzMTg0MykiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkpY8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPldFIExPVkUgTUFOQUdFUiBHQUVSV0VOSUxMPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzIwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNjAwIiBmb250LXNpemU9IjIwIiBmaWxsPSIjZTJlOGYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVEFZIEZhbiBFZGl0IOKAoiAjTWFuYWdlckdhZXJ3ZW5pbGw8L3RleHQ+Cjwvc3ZnPg==", caption: "OOTD for today's schedule 😎" }
    ];

    let posts = [
        {
            id: 1, author: "Gaerwenill", handle: "@gaerwenill", avatar: myAvatar, verified: true, time: "10m ago",
            content: "Official Announcement: Stray Kids is preparing something huge for STAYs worldwide! Stay tuned for tour dates! 🧭✨ #StrayKids #JYPE",
            image: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfNGMxZDk1IiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzRjMWQ5NSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZGIyNzc3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzRjMWQ5NSkiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfp608L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNLWiBXT1JMRCBUT1VSIDIwMjY8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIzMjAiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI2MDAiIGZvbnQtc2l6ZT0iMjAiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk9mZmljaWFsIEFubm91bmNlbWVudCDigKIgSllQIEVudGVydGFpbm1lbnQ8L3RleHQ+Cjwvc3ZnPg==",
            likes: 24800, liked: false,
            comments: [
                { author: "Bang Chan", handle: "@gnabnahc", avatar: BOTS.bangchan.avatar, text: "Let's go @gaerwenill! STAY get ready!! 🔥🔥" },
                { author: "Felix", handle: "@yong.lixx", avatar: BOTS.felix.avatar, text: "So excited!! Made brownies for @gaerwenill today! ❤️" },
                { author: "Lixxie Brownies 🍪", handle: "@felix_sunshine_stay", avatar: BOTS.stay_felix.avatar, text: "MANAGER GAERWENILL WE LOVE YOU!! THANK YOU FOR MAKING THIS HAPPEN 😭💖" }
            ]
        },
        {
            id: 2, author: "Bang Chan", handle: "@gnabnahc", avatar: BOTS.bangchan.avatar, verified: true, time: "45m ago",
            content: "Late night in the studio working on new tracks. Thank you Manager @gaerwenill for bringing iced americano! ☕🎧 #3RACHA #STAY",
            image: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfMWUzYThhIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzFlM2E4YSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMjU2M2ViIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzFlM2E4YSkiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfjqc8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPjNSQUNIQSBTVFVESU8gU0VTU0lPTjwvdGV4dD4KICA8dGV4dCB4PSI0MDAiIHk9IjMyMCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2UyZThmMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TGF0ZSBOaWdodCBQcm9kdWNpbmcg4oCiIE5ldyBBbGJ1bTwvdGV4dD4KPC9zdmc+",
            likes: 38900, liked: false,
            comments: [
                { author: "Han Jisung", handle: "@_doolsetnet", avatar: BOTS.han.avatar, text: "Save some americano for me hyung!! 🎵" },
                { author: "Chanie's Room Live 🎧", handle: "@chan_room_official", avatar: BOTS.stay_chan.avatar, text: "CHAN REST WELL PLEASE!! We love you Chanie!!" }
            ]
        },
        {
            id: 3, author: "Dispatch Official", handle: "@kpop_dispatch", avatar: BOTS.dispatch.avatar, verified: true, time: "2h ago",
            content: "🚨 BREAKING: Stray Kids Head Manager @gaerwenill spotted at JYPE Headquarters coordinating upcoming mega project! Comeback imminent?",
            image: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfOTkxYjFiIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzk5MWIxYiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZGMyNjI2IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzk5MWIxYikiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfmqg8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkRJU1BBVENIIEVYQ0xVU0lWRTwvdGV4dD4KICA8dGV4dCB4PSI0MDAiIHk9IjMyMCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iI2UyZThmMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U3RyYXkgS2lkcyBSZWhlYXJzYWwgd2l0aCBNYW5hZ2VyIEBnYWVyd2VuaWxsPC90ZXh0Pgo8L3N2Zz4=",
            likes: 51200, liked: false,
            comments: [
                { author: "STAY World Updates", handle: "@stay_updates", avatar: BOTS.stay_world.avatar, text: "MANAGER GAERWENILL IS WORKING SO HARD!! BEST MANAGER IN K-POP!!" },
                { author: "Lee Know", handle: "@t.leeknowsaurus", avatar: BOTS.leeknow.avatar, text: "Dispatch please buy us pudding next time you take photos 🥩" }
            ]
        },
        {
            id: 4, author: "Felix", handle: "@yong.lixx", avatar: BOTS.felix.avatar, verified: true, time: "3h ago",
            content: "Baked fresh homemade brownies for Manager @gaerwenill & the boys today! Hope everyone stays warm! 🍪☀️❤️",
            image: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfOWEzNDEyIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzlhMzQxMiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZWE1ODBjIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzlhMzQxMikiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfjao8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkZFTElYIEhPTUVNQURFIEJST1dOSUVTPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzIwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNjAwIiBmb250LXNpemU9IjIwIiBmaWxsPSIjZTJlOGYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5CYWtlZCB3aXRoIGxvdmUgZm9yIE1hbmFnZXIgJiBTVEFZIOKdpO+4jzwvdGV4dD4KPC9zdmc+",
            likes: 67400, liked: false,
            comments: [
                { author: "Changbin", handle: "@jutdwae", avatar: BOTS.changbin.avatar, text: "PROTEIN BROWNIES?? JUTDAE APPROVED! 💪" },
                { author: "Lixxie Brownies 🍪", handle: "@felix_sunshine_stay", avatar: BOTS.stay_felix.avatar, text: "SUNSHINE FELIX BREAD BAKING 😭 WE ARE SO BLESSED!" }
            ]
        },
        {
            id: 5, author: "SKZ 5-STAR Worldwide 🧭", handle: "@stay_forever_5star", avatar: BOTS.stay_5star.avatar, verified: false, time: "4h ago",
            content: "OMG STAYs!! Manager @gaerwenill just confirmed World Tour dates!! ARE WE READY?? 🧭✨",
            image: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDIwIiB2aWV3Qm94PSIwIDAgODAwIDQyMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfODMxODQzIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzgzMTg0MyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZGIyNzc3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0MjAiIHJ4PSIyMCIgZmlsbD0idXJsKCNwXzgzMTg0MykiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSI4MCIgcj0iMTQwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA2Ii8+CiAgPGNpcmNsZSBjeD0iNzAwIiBjeT0iMzQwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDYiLz4KICA8dGV4dCB4PSI0MDAiIHk9IjE4MCIgZm9udC1mYW1pbHk9InN5c3RlbS11aSwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkpY8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyNzUiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMzIiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPldFIExPVkUgTUFOQUdFUiBHQUVSV0VOSUxMPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzIwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNjAwIiBmb250LXNpemU9IjIwIiBmaWxsPSIjZTJlOGYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVEFZIEZhbiBFZGl0IOKAoiAjTWFuYWdlckdhZXJ3ZW5pbGw8L3RleHQ+Cjwvc3ZnPg==",
            likes: 18200, liked: false,
            comments: [
                { author: "Lixxie Brownies 🍪", handle: "@felix_sunshine_stay", avatar: BOTS.stay_felix.avatar, text: "TAKE MY MONEY!! I'M GOING TO SEE SKZ!!" }
            ]
        }
    ];

    let activeDMKey = "bangchan";
    let dmMessages = {
        "bangchan": [
            { sender: "incoming", text: "Hey Manager @gaerwenill! Thanks for coordinating the schedule today! 🐺❤️" },
            { sender: "incoming", text: "Are we still meeting in the studio at 9 PM for track review?" }
        ],
        "felix": [
            { sender: "incoming", text: "Manager @gaerwenill! I saved 3 brownies for you in the lounge! 🍪✨" }
        ],
        "leeknow": [
            { sender: "incoming", text: "Manager @gaerwenill, where is my pudding? 🐱" }
        ],
        "changbin": [
            { sender: "incoming", text: "JUTDAE! Did you see my bicep gains in the photoshoot @gaerwenill?! 💪" }
        ],
        "hyunjin": [
            { sender: "incoming", text: "KAMI BIT MY SOCK AGAIN 😭 Manager help me!" }
        ],
        "han": [
            { sender: "incoming", text: "I wrote 3 songs in my sleep last night! You're welcome @gaerwenill! 🎵" }
        ],
        "seungmin": [
            { sender: "incoming", text: "Vocal practice finished! Ready for comeback @gaerwenill. 🐶" }
        ],
        "in": [
            { sender: "incoming", text: "Look at my OOTD for today's schedule @gaerwenill! 😎👔" }
        ]
    };

    function renderStories() {
        const container = document.getElementById("storiesBar");
        container.innerHTML = STORIES.map((s, index) => `
            <div class="story-item" onclick="openStoryModal(${index})">
                <div class="story-ring">
                    <img src="${s.avatar}" class="story-avatar">
                </div>
                <div class="story-username">${s.name}</div>
            </div>
        `).join("");
    }

    function renderFeed() {
        const feed = document.getElementById("mainFeed");
        feed.innerHTML = posts.map(p => `
            <div class="post">
                <img src="${p.avatar}" class="post-avatar">
                <div class="post-content">
                    <div class="post-header">
                        <span class="post-author">${p.author}</span>
                        ${p.verified ? '<span class="verified-badge">✔</span>' : ''}
                        <span class="post-handle">${p.handle} • ${p.time}</span>
                    </div>
                    <div class="post-text">${p.content}</div>
                    ${p.image ? `<img src="${p.image}" class="post-image-card">` : ''}
                    <div class="post-actions">
                        <div class="action-item ${p.liked ? 'liked' : ''}" onclick="toggleLike(${p.id})">
                            ${p.liked ? '❤️' : '🤍'} <span>${p.likes.toLocaleString()}</span>
                        </div>
                        <div class="action-item">
                            💬 <span>${p.comments.length}</span>
                        </div>
                        <div class="action-item">
                            🔄 <span>Share</span>
                        </div>
                    </div>
                    <div class="comments-list">
                        ${p.comments.map((c, cIdx) => `
                            <div class="comment-item">
                                <img src="${c.avatar}" class="comment-avatar">
                                <div class="comment-body">
                                    <span class="comment-author">${c.author}</span>
                                    <span class="comment-handle">${c.handle}</span>
                                    <div class="comment-text">${c.text}</div>
                                    <button class="comment-reply-btn" onclick="toggleInlineReply(${p.id}, ${cIdx})">💬 Reply</button>
                                    <div class="inline-reply-box" id="replyBox_${p.id}_${cIdx}">
                                        <input type="text" id="replyInput_${p.id}_${cIdx}" class="inline-reply-input" placeholder="Reply to ${c.author}...">
                                        <button class="inline-reply-send" onclick="sendInlineReply(${p.id}, ${cIdx}, '${c.author}')">Send</button>
                                    </div>
                                </div>
                            </div>
                        `).join("")}
                    </div>
                </div>
            </div>
        `).join("");

        const userFeed = document.getElementById("userProfileFeed");
        const userPosts = posts.filter(p => p.handle === "@gaerwenill");
        if (userPosts.length === 0) {
            userFeed.innerHTML = '<div style="padding:20px; text-align:center; color:#64748b;">No posts yet. Create a post above!</div>';
        } else {
            userFeed.innerHTML = userPosts.map(p => `
                <div class="post">
                    <img src="${p.avatar}" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">${p.author}</span>
                            <span class="verified-badge">✔</span>
                            <span class="post-handle">${p.handle} • ${p.time}</span>
                        </div>
                        <div class="post-text">${p.content}</div>
                        ${p.image ? `<img src="${p.image}" class="post-image-card">` : ''}
                    </div>
                </div>
            `).join("");
        }
    }

    function toggleLike(postId) {
        const post = posts.find(p => p.id === postId);
        if (post) {
            post.liked = !post.liked;
            post.likes += post.liked ? 1 : -1;
            renderFeed();
        }
    }

    function handlePostImageUpload(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                pendingPostImg = e.target.result;
                document.getElementById("postPreviewImg").src = pendingPostImg;
                document.getElementById("postImagePreview").style.display = "block";
            };
            reader.readAsDataURL(file);
        }
    }

    function clearPostImage() {
        pendingPostImg = null;
        document.getElementById("postImagePreview").style.display = "none";
    }

    function createNewPost() {
        const text = document.getElementById("newPostText").value.trim();
        if (!text && !pendingPostImg) return;

        const newPost = {
            id: Date.now(),
            author: "Gaerwenill",
            handle: "@gaerwenill",
            avatar: myAvatar,
            verified: true,
            time: "Just now",
            content: text || "New update from Stray Kids Management! 🧭✨",
            image: pendingPostImg,
            likes: Math.floor(Math.random() * 5000) + 12000,
            liked: false,
            comments: []
        };

        posts.unshift(newPost);
        document.getElementById("newPostText").value = "";
        clearPostImage();
        renderFeed();

        setTimeout(() => {
            const randomKeys = ["bangchan", "felix", "leeknow", "changbin", "stay_world", "stay_felix", "stay_5star"];
            const selected = randomKeys.sort(() => 0.5 - Math.random()).slice(0, 3);
            
            selected.forEach(k => {
                const b = BOTS[k];
                const respList = BOT_RESPONSES[k] || ["WE LOVE YOU MANAGER GAERWENILL!! 💖"];
                const textResp = respList[Math.floor(Math.random() * respList.length)];
                newPost.comments.push({
                    author: b.name,
                    handle: b.handle,
                    avatar: b.avatar,
                    text: textResp
                });
            });
            renderFeed();
        }, 1200);
    }

    function toggleInlineReply(postId, cIdx) {
        const box = document.getElementById(`replyBox_${postId}_${cIdx}`);
        if (box) box.classList.toggle("active");
    }

    function sendInlineReply(postId, cIdx, targetAuthor) {
        const input = document.getElementById(`replyInput_${postId}_${cIdx}`);
        const text = input.value.trim();
        if (!text) return;

        const post = posts.find(p => p.id === postId);
        if (post) {
            post.comments.push({
                author: "Gaerwenill",
                handle: "@gaerwenill",
                avatar: myAvatar,
                text: `@${targetAuthor} ${text}`
            });
            renderFeed();

            setTimeout(() => {
                const botKey = Object.keys(BOTS).find(k => BOTS[k].name === targetAuthor) || "stay_world";
                const b = BOTS[botKey];
                const respList = BOT_RESPONSES[botKey] || ["Thank you Manager @gaerwenill! ❤️"];
                post.comments.push({
                    author: b.name,
                    handle: b.handle,
                    avatar: b.avatar,
                    text: `@gaerwenill ${respList[Math.floor(Math.random() * respList.length)]}`
                });
                renderFeed();
            }, 1200);
        }
    }

    let activeStoryIndex = 0;
    function openStoryModal(index) {
        activeStoryIndex = index;
        const s = STORIES[index];
        document.getElementById("storyModalAvatar").src = s.avatar;
        document.getElementById("storyModalTitle").innerText = s.name;
        document.getElementById("storyModalImg").src = s.img;
        document.getElementById("storyModal").classList.add("active");
    }

    function closeStoryModal() {
        document.getElementById("storyModal").classList.remove("active");
    }

    function sendStoryReply() {
        const input = document.getElementById("storyReplyInput");
        const val = input.value.trim();
        if (val) {
            alert(`Story reply sent to ${STORIES[activeStoryIndex].name}! ❤️`);
            input.value = "";
            closeStoryModal();
        }
    }

    function renderDMSidebar() {
        const sidebar = document.getElementById("dmSidebar");
        const members = ["bangchan", "felix", "leeknow", "changbin", "hyunjin", "han", "seungmin", "in"];
        sidebar.innerHTML = members.map(k => {
            const b = BOTS[k];
            return `
                <div class="dm-member-item ${k === activeDMKey ? 'active' : ''}" onclick="selectDMMember('${k}')">
                    <img src="${b.avatar}" class="dm-member-avatar">
                    <div class="dm-member-name">${b.name}</div>
                </div>
            `;
        }).join("");
    }

    function selectDMMember(key) {
        activeDMKey = key;
        renderDMSidebar();
        const b = BOTS[key];
        document.getElementById("activeDMAvatar").src = b.avatar;
        document.getElementById("activeDMTitle").innerText = b.name;
        renderDMMessages();
    }

    function renderDMMessages() {
        const chatBox = document.getElementById("dmMessages");
        const msgs = dmMessages[activeDMKey] || [];
        chatBox.innerHTML = msgs.map(m => `
            <div class="chat-bubble ${m.sender}">${m.text}</div>
        `).join("");
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function sendDM() {
        const input = document.getElementById("dmInput");
        const text = input.value.trim();
        if (!text) return;

        if (!dmMessages[activeDMKey]) dmMessages[activeDMKey] = [];
        dmMessages[activeDMKey].push({ sender: "outgoing", text: text });
        input.value = "";
        renderDMMessages();

        setTimeout(() => {
            const respList = BOT_RESPONSES[activeDMKey] || ["Thank you Manager @gaerwenill! ❤️"];
            dmMessages[activeDMKey].push({
                sender: "incoming",
                text: respList[Math.floor(Math.random() * respList.length)]
            });
            renderDMMessages();
        }, 1200);
    }

    function handleProfilePhotoUpload(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                myAvatar = e.target.result;
                document.getElementById("userHeaderAvatar").src = myAvatar;
                document.getElementById("userCreatePostAvatar").src = myAvatar;
                document.getElementById("userProfileAvatar").src = myAvatar;
                renderFeed();
            };
            reader.readAsDataURL(file);
        }
    }

    function switchTab(tabId) {
        document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        
        document.getElementById(tabId).classList.add('active');
        
        if (tabId === 'feedTab') document.getElementById('navFeed').classList.add('active');
        if (tabId === 'searchTab') document.getElementById('navSearch').classList.add('active');
        if (tabId === 'dmTab') {
            document.getElementById('navDMs').classList.add('active');
            selectDMMember(activeDMKey);
        }
        if (tabId === 'profileTab') document.getElementById('navProfile').classList.add('active');
    }

    renderStories();
    renderFeed();
    renderDMSidebar();
</script>
</body>
</html>"""

components.html(html_content, height=950, scrolling=True)
