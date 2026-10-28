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

html_content = """
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
            width: 34px; height: 34px; border-radius: 50%; object-fit: cover;
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
        .story-modal-img { width: 100%; height: 100%; object-fit: contain; }

        .story-modal-footer { padding: 12px 16px 20px 16px; background: rgba(0,0,0,0.8); display: flex; gap: 10px; align-items: center; }
        .story-input { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 20px; padding: 10px 16px; color: #fff; outline: none; font-size: 14px; }
        .story-send-btn { background: #a855f7; color: #fff; border: none; padding: 10px 18px; border-radius: 20px; font-weight: 700; cursor: pointer; }

        /* FEED & POSTS */
        .feed { display: flex; flex-direction: column; }
        .create-post-box { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .create-post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; border: 2px solid #a855f7; }
        .create-post-input-area { flex: 1; display: flex; flex-direction: column; gap: 10px; }
        .create-post-textarea { width: 100%; background: transparent; border: none; color: #f7f9f9; outline: none; font-size: 16px; resize: none; min-height: 50px; }
        .create-post-actions { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #16181c; pt: 10px; margin-top: 6px; padding-top: 8px; }
        .post-btn { background: #a855f7; color: white; border: none; padding: 8px 18px; border-radius: 20px; font-weight: 700; cursor: pointer; font-size: 14px; }
        .attach-btn { background: #1e293b; color: #a855f7; border: 1px solid #334155; padding: 6px 12px; border-radius: 16px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 4px; }

        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; }
        .post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #16181c; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 4px; margin-bottom: 4px; flex-wrap: wrap; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 13px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.4; color: #e7e9ea; margin-bottom: 10px; white-space: pre-wrap; }
        .post-image-card { width: 100%; border-radius: 16px; margin-bottom: 10px; border: 1px solid #2f3336; object-fit: cover; max-height: 320px; }

        .post-actions { display: flex; justify-content: space-between; max-width: 360px; color: #71767b; font-size: 13px; margin-top: 8px; }
        .action-item { display: flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px; transition: color 0.2s; }
        .action-item:hover { color: #a855f7; }
        .action-item.liked { color: #f91880; font-weight: bold; }

        /* COMMENTS */
        .comments-list { margin-top: 12px; border-top: 1px solid #16181c; padding-top: 10px; display: flex; flex-direction: column; gap: 10px; }
        .comment-item { display: flex; gap: 10px; background: #0b0e14; padding: 10px 12px; border-radius: 12px; border: 1px solid #1e293b; }
        .comment-avatar { width: 32px; height: 32px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
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
        .profile-cam-btn { position: absolute; bottom: 2px; right: 2px; background: #a855f7; color: #fff; border: 2px solid #000; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; cursor: pointer; shadow: 0 2px 6px rgba(0,0,0,0.5); }
        
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
    <!-- FILE INPUTS FOR UPLOADS -->
    <input type="file" id="profile-upload" accept="image/*" style="display:none;" onchange="uploadProfilePhoto(event)">
    <input type="file" id="post-upload" accept="image/*" style="display:none;" onchange="uploadPostPhoto(event)">

    <div class="app-container">
        <!-- TOP HEADER -->
        <div class="top-header">
            <div class="app-logo"><span>✨ Status AI</span></div>
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="color:#a855f7; font-size: 12px; font-weight: 800; background: rgba(168,85,247,0.15); padding: 4px 10px; border-radius: 12px; border: 1px solid rgba(168,85,247,0.3);">⚡ UNLIMITED ENERGY</span>
                <img id="header-my-avatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ2FlcndlbmlsbCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM5MzMzRUEiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0VDNDg5OSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2dhZXJ3ZW5pbGwiIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19nYWVyd2VuaWxsKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9nYWVyd2VuaWxsKSI+R1c8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+RkTwvdGV4dD4KPC9zdmc+" class="header-avatar" onclick="switchTab('profile')" title="View Profile">
            </div>
        </div>

        <!-- TAB 1: FEED -->
        <div id="tab-feed" class="tab-content active">
            <!-- STORIES CAROUSEL -->
            <div class="stories-container">
                <div class="story-item" onclick="openStory('gaerwenill')">
                    <div class="story-ring"><img id="story-my-avatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ2FlcndlbmlsbCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM5MzMzRUEiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0VDNDg5OSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2dhZXJ3ZW5pbGwiIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19nYWVyd2VuaWxsKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9nYWVyd2VuaWxsKSI+R1c8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+RkTwvdGV4dD4KPC9zdmc+" class="story-avatar"></div>
                    <span class="story-username">@gaerwenill</span>
                </div>
                <div class="story-item" onclick="openStory('chan')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+" class="story-avatar"></div>
                    <span class="story-username">gnabnahc</span>
                </div>
                <div class="story-item" onclick="openStory('felix')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmVsaXgiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDNGNUUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9mZWxpeCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2ZlbGl4KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9mZWxpeCkiPkZMPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkKU8L3RleHQ+Cjwvc3ZnPg==" class="story-avatar"></div>
                    <span class="story-username">yong.lixx</span>
                </div>
                <div class="story-item" onclick="openStory('leeknow')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfbGVla25vdyIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMwNTk2NjkiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzEwQjk4MSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2xlZWtub3ciIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19sZWVrbm93KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9sZWVrbm93KSI+TEs8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QsTwvdGV4dD4KPC9zdmc+" class="story-avatar"></div>
                    <span class="story-username">t.leeknow</span>
                </div>
                <div class="story-item" onclick="openStory('hyunjin')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaHl1bmppbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNEOTc3MDYiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzhCNUNGNiIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2h5dW5qaW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19oeXVuamluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oeXVuamluKSI+SEo8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+lnzwvdGV4dD4KPC9zdmc+" class="story-avatar"></div>
                    <span class="story-username">hynjinnnn</span>
                </div>
                <div class="story-item" onclick="openStory('han')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaGFuIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzI1NjNFQiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDZCNkQ0IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxmaWx0ZXIgaWQ9ImZfaGFuIiB4PSItMjAlIiB5PSItMjAlIiB3aWR0aD0iMTQwJSIgaGVpZ2h0PSIxNDAlIj4KICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iNiIgZmxvb2QtY29sb3I9IiMwMDAiIGZsb29kLW9wYWNpdHk9IjAuNiIvPgogICAgPC9maWx0ZXI+CiAgPC9kZWZzPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjEwMCIgcj0iMTAwIiBmaWxsPSJ1cmwoI2dfaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oYW4pIj5KUzwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0MiIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjI4IiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn6aYPC90ZXh0Pgo8L3N2Zz4=" class="story-avatar"></div>
                    <span class="story-username">_doolsetnet</span>
                </div>
                <div class="story-item" onclick="openStory('changbin')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbmdiaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjREMyNjI2IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNTlFMEIiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9jaGFuZ2JpbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2NoYW5nYmluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuZ2JpbikiPkNCPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLfwn5CwPC90ZXh0Pgo8L3N2Zz4=" class="story-avatar"></div>
                    <span class="story-username">jutdwae</span>
                </div>
                <div class="story-item" onclick="openStory('seungmin')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc2V1bmdtaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMDI4NEM3IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMzOEJERjgiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9zZXVuZ21pbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX3NldW5nbWluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9zZXVuZ21pbikiPlNNPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLY8L3RleHQ+Cjwvc3ZnPg==" class="story-avatar"></div>
                    <span class="story-username">miniverse.___</span>
                </div>
                <div class="story-item" onclick="openStory('in')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRUE1ODBDIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGOTczMTYiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9pbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2luKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9pbikiPklOPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfpoo8L3RleHQ+Cjwvc3ZnPg==" class="story-avatar"></div>
                    <span class="story-username">i.2.n.8</span>
                </div>
                <div class="story-item" onclick="openStory('dispatch')">
                    <div class="story-ring"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZGlzcGF0Y2giIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMxMTE4MjciIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9kaXNwYXRjaCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2Rpc3BhdGNoKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9kaXNwYXRjaCkiPkQ8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+aqDwvdGV4dD4KPC9zdmc+" class="story-avatar"></div>
                    <span class="story-username">kpop_dispatch</span>
                </div>
            </div>

            <!-- CREATE POST BOX -->
            <div class="create-post-box">
                <img id="create-my-avatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ2FlcndlbmlsbCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM5MzMzRUEiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0VDNDg5OSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2dhZXJ3ZW5pbGwiIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19nYWVyd2VuaWxsKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9nYWVyd2VuaWxsKSI+R1c8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+RkTwvdGV4dD4KPC9zdmc+" class="create-post-avatar">
                <div class="create-post-input-area">
                    <textarea id="new-post-text" class="create-post-textarea" placeholder="Post update as Head Manager @gaerwenill..."></textarea>
                    <div id="post-img-preview-container" style="display:none; position:relative; width:100%; max-height:200px; overflow:hidden; border-radius:12px; margin-bottom:8px;">
                        <img id="post-img-preview" src="" style="width:100%; object-fit:cover;">
                        <button onclick="removePostImg()" style="position:absolute; top:8px; right:8px; background:rgba(0,0,0,0.8); color:#fff; border:none; border-radius:50%; width:26px; height:26px; cursor:pointer;">✕</button>
                    </div>
                    <div class="create-post-actions">
                        <button class="attach-btn" onclick="document.getElementById('post-upload').click()">📷 Add Photo</button>
                        <button class="post-btn" onclick="createNewPost()">Post Update</button>
                    </div>
                </div>
            </div>

            <!-- FEED POSTS -->
            <div class="feed" id="feed-container">
                <!-- POST 1: BANG CHAN -->
                <div class="post" id="post-1">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Bang Chan</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@gnabnahc · 15m</span>
                        </div>
                        <div class="post-text">Huge shoutout to our Head Manager @gaerwenill for organizing the entire world tour schedule! STAYs, get ready for the ultimate stage! 🔥❤️</div>
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfZ3JhZF/wn4+f77iPIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzNiMDc2NCIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMGYxNzJhIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0NTAiIGZpbGw9InVybCgjcF9ncmFkX/Cfj5/vuI8pIi8+CiAgPHJlY3QgeD0iMjAiIHk9IjIwIiB3aWR0aD0iNzYwIiBoZWlnaHQ9IjQxMCIgcng9IjE2IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjMiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLW9wYWNpdHk9IjAuMiIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMTgwIiBmb250LXNpemU9IjgwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn4+f77iPPC90ZXh0PgogIDxyZWN0IHg9IjI1MCIgeT0iMjIwIiB3aWR0aD0iMzAwIiBoZWlnaHQ9IjM2IiByeD0iMTgiIGZpbGw9IiNhODU1ZjciLz4KICA8dGV4dCB4PSI0MDAiIHk9IjI0NCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5MSVZFIFNUQUdFPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzEwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPldPUkxEIFRPVVIgMjAyNiBTVEFHRSBSRUhFQVJTQUw8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIzNTAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjYwMCIgZm9udC1zaXplPSIxNiIgZmlsbD0iI2NiZDVlMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U1RSQVkgS0lEUyBPRkZJQ0lBTCBNRURJQSDCtyBTVEFUVVMgQUk8L3RleHQ+Cjwvc3ZnPg==" class="post-image-card">
                        <div class="post-actions">
                            <div class="action-item">💬 <span id="comments-count-1">3</span></div>
                            <div class="action-item">🔄 8,910</div>
                            <div class="action-item" onclick="toggleLike(this, 1)">❤️ <span class="like-num">45.2K</span></div>
                        </div>

                        <!-- COMMENTS THREAD -->
                        <div class="comments-list" id="comments-list-1">
                            <div class="comment-item">
                                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmVsaXgiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDNGNUUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9mZWxpeCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2ZlbGl4KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9mZWxpeCkiPkZMPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkKU8L3RleHQ+Cjwvc3ZnPg==" class="comment-avatar">
                                <div class="comment-body">
                                    <div class="comment-author">Felix <span class="verified-badge">☑️</span> <span class="comment-handle">@yong.lixx</span></div>
                                    <div class="comment-text">Manager @gaerwenill worked so hard! Made extra brownies for everyone! 🍪✨</div>
                                    <button class="comment-reply-btn" onclick="toggleReplyBox('reply-box-1-1')">💬 Reply</button>
                                    <div class="inline-reply-box" id="reply-box-1-1">
                                        <input type="text" class="inline-reply-input" id="reply-input-1-1" placeholder="Reply to @yong.lixx as @gaerwenill...">
                                        <button class="inline-reply-send" onclick="sendReply(1, 'Felix', '@yong.lixx', 'reply-input-1-1', 'reply-box-1-1')">Send</button>
                                    </div>
                                </div>
                            </div>

                            <div class="comment-item">
                                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfbGVla25vdyIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMwNTk2NjkiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzEwQjk4MSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2xlZWtub3ciIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19sZWVrbm93KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9sZWVrbm93KSI+TEs8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QsTwvdGV4dD4KPC9zdmc+" class="comment-avatar">
                                <div class="comment-body">
                                    <div class="comment-author">Lee Know <span class="verified-badge">☑️</span> <span class="comment-handle">@t.leeknow</span></div>
                                    <div class="comment-text">Great job @gaerwenill. Now please order meat for dinner. 🥩</div>
                                    <button class="comment-reply-btn" onclick="toggleReplyBox('reply-box-1-2')">💬 Reply</button>
                                    <div class="inline-reply-box" id="reply-box-1-2">
                                        <input type="text" class="inline-reply-input" id="reply-input-1-2" placeholder="Reply to @t.leeknow as @gaerwenill...">
                                        <button class="inline-reply-send" onclick="sendReply(1, 'Lee Know', '@t.leeknow', 'reply-input-1-2', 'reply-box-1-2')">Send</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- POST 2: FELIX -->
                <div class="post" id="post-2">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmVsaXgiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDNGNUUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9mZWxpeCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2ZlbGl4KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9mZWxpeCkiPkZMPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkKU8L3RleHQ+Cjwvc3ZnPg==" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Felix</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@yong.lixx · 45m</span>
                        </div>
                        <div class="post-text">Baked fresh chocolate brownies for @gaerwenill and the boys after practice today! Hope everyone stays warm and happy! ✨🍪</div>
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfZ3JhZF/wn42qIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzgzMTg0MyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMzEwZTIxIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0NTAiIGZpbGw9InVybCgjcF9ncmFkX/CfjaopIi8+CiAgPHJlY3QgeD0iMjAiIHk9IjIwIiB3aWR0aD0iNzYwIiBoZWlnaHQ9IjQxMCIgcng9IjE2IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjMiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLW9wYWNpdHk9IjAuMiIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMTgwIiBmb250LXNpemU9IjgwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn42qPC90ZXh0PgogIDxyZWN0IHg9IjI1MCIgeT0iMjIwIiB3aWR0aD0iMzAwIiBoZWlnaHQ9IjM2IiByeD0iMTgiIGZpbGw9IiNhODU1ZjciLz4KICA8dGV4dCB4PSI0MDAiIHk9IjI0NCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5GRUxJWCBCQUtFUlkg8J+NqjwvdGV4dD4KICA8dGV4dCB4PSI0MDAiIHk9IjMxMCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjI4IiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5GUkVTSCBCUk9XTklFUyBGT1IgTUFOQUdFUiBAR0FFUldFTklMTDwvdGV4dD4KICA8dGV4dCB4PSI0MDAiIHk9IjM1MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNjAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjY2JkNWUxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVFJBWSBLSURTIE9GRklDSUFMIE1FRElBIMK3IFNUQVRVUyBBSTwvdGV4dD4KPC9zdmc+" class="post-image-card">
                        <div class="post-actions">
                            <div class="action-item">💬 <span id="comments-count-2">2</span></div>
                            <div class="action-item">🔄 12.4K</div>
                            <div class="action-item" onclick="toggleLike(this, 2)">❤️ <span class="like-num">89.1K</span></div>
                        </div>

                        <div class="comments-list" id="comments-list-2">
                            <div class="comment-item">
                                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbmdiaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjREMyNjI2IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNTlFMEIiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9jaGFuZ2JpbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2NoYW5nYmluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuZ2JpbikiPkNCPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLfwn5CwPC90ZXh0Pgo8L3N2Zz4=" class="comment-avatar">
                                <div class="comment-body">
                                    <div class="comment-author">Changbin <span class="verified-badge">☑️</span> <span class="comment-handle">@jutdwae</span></div>
                                    <div class="comment-text">Are these protein brownies? Save 5 for me @yong.lixx! 💪</div>
                                    <button class="comment-reply-btn" onclick="toggleReplyBox('reply-box-2-1')">💬 Reply</button>
                                    <div class="inline-reply-box" id="reply-box-2-1">
                                        <input type="text" class="inline-reply-input" id="reply-input-2-1" placeholder="Reply to @jutdwae as @gaerwenill...">
                                        <button class="inline-reply-send" onclick="sendReply(2, 'Changbin', '@jutdwae', 'reply-input-2-1', 'reply-box-2-1')">Send</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- POST 3: DISPATCH -->
                <div class="post" id="post-3">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZGlzcGF0Y2giIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMxMTE4MjciIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9kaXNwYXRjaCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2Rpc3BhdGNoKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9kaXNwYXRjaCkiPkQ8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+aqDwvdGV4dD4KPC9zdmc+" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Dispatch Official</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@kpop_dispatch · 2h</span>
                        </div>
                        <div class="post-text">🚨 BREAKING EXCLUSIVE: Stray Kids Head Manager @gaerwenill spotted arriving at JYP Entertainment for final tour meetings!</div>
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MDAiIGhlaWdodD0iNDUwIiB2aWV3Qm94PSIwIDAgODAwIDQ1MCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InBfZ3JhZF/wn5O4IiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzdmMWQxZCIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDAwMDAwIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI0NTAiIGZpbGw9InVybCgjcF9ncmFkX/Cfk7gpIi8+CiAgPHJlY3QgeD0iMjAiIHk9IjIwIiB3aWR0aD0iNzYwIiBoZWlnaHQ9IjQxMCIgcng9IjE2IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjMiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLW9wYWNpdHk9IjAuMiIvPgogIDx0ZXh0IHg9IjQwMCIgeT0iMTgwIiBmb250LXNpemU9IjgwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn5O4PC90ZXh0PgogIDxyZWN0IHg9IjI1MCIgeT0iMjIwIiB3aWR0aD0iMzAwIiBoZWlnaHQ9IjM2IiByeD0iMTgiIGZpbGw9IiNhODU1ZjciLz4KICA8dGV4dCB4PSI0MDAiIHk9IjI0NCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5ESVNQQVRDSCBCUkVBS0lORyDwn5qoPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzEwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkVYQ0xVU0lWRTogTUFOQUdFUiBAR0FFUldFTklMTCBBVCBKWVBFPC90ZXh0PgogIDx0ZXh0IHg9IjQwMCIgeT0iMzUwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI2MDAiIGZvbnQtc2l6ZT0iMTYiIGZpbGw9IiNjYmQ1ZTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNUUkFZIEtJRFMgT0ZGSUNJQUwgTUVESUEgwrcgU1RBVFVTIEFJPC90ZXh0Pgo8L3N2Zz4=" class="post-image-card">
                        <div class="post-actions">
                            <div class="action-item">💬 <span id="comments-count-3">1</span></div>
                            <div class="action-item">🔄 34.2K</div>
                            <div class="action-item" onclick="toggleLike(this, 3)">❤️ <span class="like-num">120.5K</span></div>
                        </div>

                        <div class="comments-list" id="comments-list-3">
                            <div class="comment-item">
                                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc3RheTEiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjQzA4NEZDIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDcyQjYiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9zdGF5MSIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX3N0YXkxKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9zdGF5MSkiPlNUPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkpY8L3RleHQ+Cjwvc3ZnPg==" class="comment-avatar">
                                <div class="comment-body">
                                    <div class="comment-author">STAY World <span class="comment-handle">@stay_updates</span></div>
                                    <div class="comment-text">WE LOVE YOU MANAGER @GAERWENILL! THANK YOU FOR PROTECTING OUR BOYS! 💖✨</div>
                                    <button class="comment-reply-btn" onclick="toggleReplyBox('reply-box-3-1')">💬 Reply</button>
                                    <div class="inline-reply-box" id="reply-box-3-1">
                                        <input type="text" class="inline-reply-input" id="reply-input-3-1" placeholder="Reply to @stay_updates as @gaerwenill...">
                                        <button class="inline-reply-send" onclick="sendReply(3, 'STAY World', '@stay_updates', 'reply-input-3-1', 'reply-box-3-1')">Send</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 2: STORIES FULL TAB -->
        <div id="tab-stories" class="tab-content">
            <div style="padding: 16px; font-weight: 900; font-size: 18px; border-bottom: 1px solid #16181c;">
                📸 Recent Stray Kids Stories
            </div>
            <div style="padding: 16px; display: flex; flex-direction: column; gap: 12px;">
                <div style="background:#111827; padding:12px; border-radius:12px; display:flex; align-items:center; gap:12px; cursor:pointer;" onclick="openStory('chan')">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+" style="width:48px; height:48px; border-radius:50%; object-fit:cover;">
                    <div>
                        <div style="font-weight:700;">Bang Chan (@gnabnahc)</div>
                        <div style="font-size:12px; color:#94a3b8;">3RACHA Studio Session 🎧</div>
                    </div>
                </div>
                <div style="background:#111827; padding:12px; border-radius:12px; display:flex; align-items:center; gap:12px; cursor:pointer;" onclick="openStory('felix')">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmVsaXgiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDNGNUUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9mZWxpeCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2ZlbGl4KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9mZWxpeCkiPkZMPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkKU8L3RleHQ+Cjwvc3ZnPg==" style="width:48px; height:48px; border-radius:50%; object-fit:cover;">
                    <div>
                        <div style="font-weight:700;">Felix (@yong.lixx)</div>
                        <div style="font-size:12px; color:#94a3b8;">Fresh Brownies Baking 🍪</div>
                    </div>
                </div>
                <div style="background:#111827; padding:12px; border-radius:12px; display:flex; align-items:center; gap:12px; cursor:pointer;" onclick="openStory('leeknow')">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfbGVla25vdyIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMwNTk2NjkiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzEwQjk4MSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2xlZWtub3ciIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19sZWVrbm93KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9sZWVrbm93KSI+TEs8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QsTwvdGV4dD4KPC9zdmc+" style="width:48px; height:48px; border-radius:50%; object-fit:cover;">
                    <div>
                        <div style="font-weight:700;">Lee Know (@t.leeknow)</div>
                        <div style="font-size:12px; color:#94a3b8;">Cats Corner 🐱</div>
                    </div>
                </div>
                <div style="background:#111827; padding:12px; border-radius:12px; display:flex; align-items:center; gap:12px; cursor:pointer;" onclick="openStory('hyunjin')">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaHl1bmppbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNEOTc3MDYiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzhCNUNGNiIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2h5dW5qaW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19oeXVuamluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oeXVuamluKSI+SEo8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+lnzwvdGV4dD4KPC9zdmc+" style="width:48px; height:48px; border-radius:50%; object-fit:cover;">
                    <div>
                        <div style="font-weight:700;">Hyunjin (@hynjinnnn)</div>
                        <div style="font-size:12px; color:#94a3b8;">Art Canvas Session 🎨</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 3: DMS TAB -->
        <div id="tab-dms" class="tab-content">
            <div class="dm-layout">
                <!-- DM SIDEBAR MEMBERS -->
                <div class="dm-sidebar">
                    <div class="dm-member-item active" onclick="selectDMChat('chan', 'Bang Chan', 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+', '@gnabnahc', this)">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+" class="dm-member-avatar">
                        <span class="dm-member-name">Bang Chan</span>
                    </div>
                    <div class="dm-member-item" onclick="selectDMChat('felix', 'Felix', 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmVsaXgiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDNGNUUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9mZWxpeCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2ZlbGl4KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9mZWxpeCkiPkZMPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkKU8L3RleHQ+Cjwvc3ZnPg==', '@yong.lixx', this)">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmVsaXgiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDNGNUUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9mZWxpeCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2ZlbGl4KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9mZWxpeCkiPkZMPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkKU8L3RleHQ+Cjwvc3ZnPg==" class="dm-member-avatar">
                        <span class="dm-member-name">Felix</span>
                    </div>
                    <div class="dm-member-item" onclick="selectDMChat('leeknow', 'Lee Know', 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfbGVla25vdyIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMwNTk2NjkiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzEwQjk4MSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2xlZWtub3ciIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19sZWVrbm93KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9sZWVrbm93KSI+TEs8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QsTwvdGV4dD4KPC9zdmc+', '@t.leeknow', this)">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfbGVla25vdyIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMwNTk2NjkiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzEwQjk4MSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2xlZWtub3ciIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19sZWVrbm93KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9sZWVrbm93KSI+TEs8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QsTwvdGV4dD4KPC9zdmc+" class="dm-member-avatar">
                        <span class="dm-member-name">Lee Know</span>
                    </div>
                    <div class="dm-member-item" onclick="selectDMChat('hyunjin', 'Hyunjin', 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaHl1bmppbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNEOTc3MDYiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzhCNUNGNiIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2h5dW5qaW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19oeXVuamluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oeXVuamluKSI+SEo8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+lnzwvdGV4dD4KPC9zdmc+', '@hynjinnnn', this)">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaHl1bmppbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNEOTc3MDYiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzhCNUNGNiIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2h5dW5qaW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19oeXVuamluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oeXVuamluKSI+SEo8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+lnzwvdGV4dD4KPC9zdmc+" class="dm-member-avatar">
                        <span class="dm-member-name">Hyunjin</span>
                    </div>
                    <div class="dm-member-item" onclick="selectDMChat('han', 'Han Jisung', 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaGFuIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzI1NjNFQiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDZCNkQ0IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxmaWx0ZXIgaWQ9ImZfaGFuIiB4PSItMjAlIiB5PSItMjAlIiB3aWR0aD0iMTQwJSIgaGVpZ2h0PSIxNDAlIj4KICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iNiIgZmxvb2QtY29sb3I9IiMwMDAiIGZsb29kLW9wYWNpdHk9IjAuNiIvPgogICAgPC9maWx0ZXI+CiAgPC9kZWZzPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjEwMCIgcj0iMTAwIiBmaWxsPSJ1cmwoI2dfaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oYW4pIj5KUzwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0MiIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjI4IiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn6aYPC90ZXh0Pgo8L3N2Zz4=', '@_doolsetnet', this)">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaGFuIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzI1NjNFQiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDZCNkQ0IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxmaWx0ZXIgaWQ9ImZfaGFuIiB4PSItMjAlIiB5PSItMjAlIiB3aWR0aD0iMTQwJSIgaGVpZ2h0PSIxNDAlIj4KICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iNiIgZmxvb2QtY29sb3I9IiMwMDAiIGZsb29kLW9wYWNpdHk9IjAuNiIvPgogICAgPC9maWx0ZXI+CiAgPC9kZWZzPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjEwMCIgcj0iMTAwIiBmaWxsPSJ1cmwoI2dfaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oYW4pIj5KUzwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0MiIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjI4IiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn6aYPC90ZXh0Pgo8L3N2Zz4=" class="dm-member-avatar">
                        <span class="dm-member-name">Han Jisung</span>
                    </div>
                    <div class="dm-member-item" onclick="selectDMChat('changbin', 'Changbin', 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbmdiaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjREMyNjI2IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNTlFMEIiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9jaGFuZ2JpbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2NoYW5nYmluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuZ2JpbikiPkNCPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLfwn5CwPC90ZXh0Pgo8L3N2Zz4=', '@jutdwae', this)">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbmdiaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjREMyNjI2IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNTlFMEIiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9jaGFuZ2JpbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2NoYW5nYmluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuZ2JpbikiPkNCPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLfwn5CwPC90ZXh0Pgo8L3N2Zz4=" class="dm-member-avatar">
                        <span class="dm-member-name">Changbin</span>
                    </div>
                    <div class="dm-member-item" onclick="selectDMChat('seungmin', 'Seungmin', 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc2V1bmdtaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMDI4NEM3IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMzOEJERjgiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9zZXVuZ21pbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX3NldW5nbWluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9zZXVuZ21pbikiPlNNPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLY8L3RleHQ+Cjwvc3ZnPg==', '@miniverse.___', this)">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc2V1bmdtaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMDI4NEM3IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMzOEJERjgiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9zZXVuZ21pbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX3NldW5nbWluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9zZXVuZ21pbikiPlNNPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLY8L3RleHQ+Cjwvc3ZnPg==" class="dm-member-avatar">
                        <span class="dm-member-name">Seungmin</span>
                    </div>
                    <div class="dm-member-item" onclick="selectDMChat('in', 'I.N', 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRUE1ODBDIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGOTczMTYiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9pbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2luKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9pbikiPklOPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfpoo8L3RleHQ+Cjwvc3ZnPg==', '@i.2.n.8', this)">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRUE1ODBDIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGOTczMTYiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9pbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2luKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9pbikiPklOPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfpoo8L3RleHQ+Cjwvc3ZnPg==" class="dm-member-avatar">
                        <span class="dm-member-name">I.N</span>
                    </div>
                </div>

                <!-- DM CHAT AREA -->
                <div class="dm-chat-area">
                    <div class="dm-chat-header">
                        <img id="dm-active-avatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+" class="dm-chat-avatar">
                        <div>
                            <div class="dm-chat-title" id="dm-active-title">Bang Chan <span class="verified-badge">☑️</span></div>
                            <div class="dm-chat-status">🟢 Active Now · SKZ Leader</div>
                        </div>
                    </div>

                    <div class="dm-chat-messages" id="dm-chat-box">
                        <div class="chat-bubble incoming">
                            <strong>Bang Chan (@gnabnahc):</strong><br>
                            Hey Manager @gaerwenill! Thanks for checking in. We just finished track #3 recording. Do you have a second to review tomorrow's photoshoot timeline?
                        </div>
                    </div>

                    <div class="dm-input-bar">
                        <input type="text" id="dm-text-input" class="dm-input" placeholder="Message as @gaerwenill..." onkeypress="if(event.key==='Enter') sendDM()">
                        <button class="dm-send-btn" onclick="sendDM()">Send</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 4: PROFILE -->
        <div id="tab-profile" class="tab-content">
            <div class="profile-container">
                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5MDAiIGhlaWdodD0iMzAwIiB2aWV3Qm94PSIwIDAgOTAwIDMwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJfZ3JhZCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM0YzFkOTUiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iNTAlIiBzdG9wLWNvbG9yPSIjODMxODQzIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwZjE3MmEiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjMwMCIgZmlsbD0idXJsKCNiX2dyYWQpIi8+CiAgPGNpcmNsZSBjeD0iMTUwIiBjeT0iMTUwIiByPSIxMDAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDUiLz4KICA8Y2lyY2xlIGN4PSI3NTAiIGN5PSIxNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4wNSIvPgogIDx0ZXh0IHg9IjQ1MCIgeT0iMTYwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iNDIiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNUUkFZIEtJRFMgSEVBRCBNQU5BR0VSPC90ZXh0Pgo8L3N2Zz4=" class="profile-banner">
                <div class="profile-header">
                    <div class="profile-avatar-wrapper">
                        <img id="profile-main-avatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ2FlcndlbmlsbCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM5MzMzRUEiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0VDNDg5OSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2dhZXJ3ZW5pbGwiIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19nYWVyd2VuaWxsKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9nYWVyd2VuaWxsKSI+R1c8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+RkTwvdGV4dD4KPC9zdmc+" class="profile-avatar">
                        <div class="profile-cam-btn" onclick="document.getElementById('profile-upload').click()" title="Change Profile Photo">📷</div>
                    </div>
                    <div class="profile-name">Gaerwenill <span class="verified-badge">☑️</span></div>
                    <div class="profile-handle">@gaerwenill</div>
                    <div class="profile-bio">
                        🧭 Official Head Manager of Stray Kids | JYP Entertainment<br>
                        Managing world tours, production schedules & member care.
                    </div>
                    <div class="profile-stats">
                        <div><span class="profile-stat-num">18.4K</span> Posts</div>
                        <div><span class="profile-stat-num">4.2M</span> Followers</div>
                        <div><span class="profile-stat-num">8</span> Following</div>
                    </div>
                </div>

                <div style="padding:16px; font-weight:800; font-size:16px; border-bottom:1px solid #16181c;">
                    Your Posts (@gaerwenill)
                </div>
                <div class="feed" id="user-posts-container">
                    <div style="padding:20px; text-align:center; color:#64748b; font-size:14px;">
                        You haven't posted any updates yet today. Use the Feed tab to post!
                    </div>
                </div>
            </div>
        </div>

        <!-- BOTTOM NAV -->
        <div class="bottom-nav">
            <a class="nav-item active" id="nav-feed" onclick="switchTab('feed')"><span class="nav-icon">🏠</span><span>Feed</span></a>
            <a class="nav-item" id="nav-stories" onclick="switchTab('stories')"><span class="nav-icon">📸</span><span>Stories</span></a>
            <a class="nav-item" id="nav-dms" onclick="switchTab('dms')"><span class="nav-icon">💬</span><span>DMs</span></a>
            <a class="nav-item" id="nav-profile" onclick="switchTab('profile')"><span class="nav-icon">👤</span><span>Profile</span></a>
        </div>
    </div>

    <!-- FULLSCREEN STORY MODAL -->
    <div class="story-modal" id="story-modal">
        <div class="story-modal-content">
            <div class="story-progress-bar"><div class="story-progress-fill" id="story-timer"></div></div>
            <div class="story-modal-header">
                <div class="story-modal-user">
                    <img id="modal-story-avatar" src="" class="story-modal-avatar">
                    <div>
                        <div id="modal-story-title" class="story-modal-title">Bang Chan</div>
                        <div id="modal-story-time" class="story-modal-time">2h ago</div>
                    </div>
                </div>
                <button class="story-close-btn" onclick="closeStory()">✕</button>
            </div>
            <div class="story-modal-body">
                <img id="modal-story-img" src="" class="story-modal-img">
            </div>
            <div class="story-modal-footer">
                <input type="text" id="story-reply-input" class="story-input" placeholder="Reply to story as @gaerwenill...">
                <button class="story-send-btn" onclick="sendStoryReply()">Reply</button>
            </div>
        </div>
    </div>

    <script>
        let myAvatarUrl = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZ2FlcndlbmlsbCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM5MzMzRUEiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0VDNDg5OSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2dhZXJ3ZW5pbGwiIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19nYWVyd2VuaWxsKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9nYWVyd2VuaWxsKSI+R1c8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+RkTwvdGV4dD4KPC9zdmc+";
        let currentPostImg = "";
        let activeDMKey = "chan";

        const STORY_DATA = {
            'gaerwenill': { title: "Gaerwenill (@gaerwenill)", avatar: myAvatarUrl, img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5MDAiIGhlaWdodD0iMzAwIiB2aWV3Qm94PSIwIDAgOTAwIDMwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJfZ3JhZCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM0YzFkOTUiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iNTAlIiBzdG9wLWNvbG9yPSIjODMxODQzIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwZjE3MmEiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjMwMCIgZmlsbD0idXJsKCNiX2dyYWQpIi8+CiAgPGNpcmNsZSBjeD0iMTUwIiBjeT0iMTUwIiByPSIxMDAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDUiLz4KICA8Y2lyY2xlIGN4PSI3NTAiIGN5PSIxNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4wNSIvPgogIDx0ZXh0IHg9IjQ1MCIgeT0iMTYwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iNDIiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNUUkFZIEtJRFMgSEVBRCBNQU5BR0VSPC90ZXh0Pgo8L3N2Zz4=", time: "10m ago" },
            'chan': { title: "Bang Chan (@gnabnahc)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/wn46b77iPIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzJlMTA2NSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMGYxNzJhIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI5MDAiIGZpbGw9InVybCgjc19ncmFkX/CfjpvvuI8pIi8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDgiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIzNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4xMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iMzgwIiBmb250LXNpemU9IjEyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+Om++4jzwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+M1JBQ0hBIFNUVURJTzwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjY5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjIyIiBmaWxsPSIjZTJlOGYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5MYXRlIE5pZ2h0IFByb2R1Y2luZyBTZXNzaW9uIPCfjqc8L3RleHQ+CiAgPGxpbmUgeDE9IjEwMCIgeTE9IjcyMCIgeDI9IjUwMCIgeTI9IjcyMCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utb3BhY2l0eT0iMC4zIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSIzMDAiIHk9Ijc3MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNTAwIiBmb250LXNpemU9IjE4IiBmaWxsPSIjY2JkNWUxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5Xb3JraW5nIG9uIHRyYWNrICMzIGZvciBTVEFZcy4uLjwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjgxMCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjYTg1NWY3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVFJBWSBLSURTIE9GRklDSUFMIFNUT1JZIPCfp608L3RleHQ+Cjwvc3ZnPg==", time: "1h ago" },
            'felix': { title: "Felix (@yong.lixx)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmVsaXgiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDNGNUUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9mZWxpeCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2ZlbGl4KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9mZWxpeCkiPkZMPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkKU8L3RleHQ+Cjwvc3ZnPg==", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/wn42qIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzg4MTMzNyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNGMwNTE5IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI5MDAiIGZpbGw9InVybCgjc19ncmFkX/CfjaopIi8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDgiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIzNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4xMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iMzgwIiBmb250LXNpemU9IjEyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+NqjwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QkFLSU5HIERBWSDwn42qPC90ZXh0PgogIDx0ZXh0IHg9IjMwMCIgeT0iNjkwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjIiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkhvbWVtYWRlIENob2NvbGF0ZSBCcm93bmllczwvdGV4dD4KICA8bGluZSB4MT0iMTAwIiB5MT0iNzIwIiB4Mj0iNTAwIiB5Mj0iNzIwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1vcGFjaXR5PSIwLjMiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iNzcwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI1MDAiIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiNjYmQ1ZTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk1hZGUgd2l0aCBsb3ZlIGZvciBNYW5hZ2VyIEBnYWVyd2VuaWxsITwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjgxMCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjYTg1NWY3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVFJBWSBLSURTIE9GRklDSUFMIFNUT1JZIPCfp608L3RleHQ+Cjwvc3ZnPg==", time: "2h ago" },
            'leeknow': { title: "Lee Know (@t.leeknow)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfbGVla25vdyIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMwNTk2NjkiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzEwQjk4MSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2xlZWtub3ciIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19sZWVrbm93KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9sZWVrbm93KSI+TEs8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QsTwvdGV4dD4KPC9zdmc+", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/wn5CxIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzA2NGUzYiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDIyYzIyIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI5MDAiIGZpbGw9InVybCgjc19ncmFkX/CfkLEpIi8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDgiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIzNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4xMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iMzgwIiBmb250LXNpemU9IjEyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QsTwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q0FUIENPUk5FUiDwn5CxPC90ZXh0PgogIDx0ZXh0IHg9IjMwMCIgeT0iNjkwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjIiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNvb25pLCBEb29uZ2kgJiBEb3JpIFNheXMgSGkhPC90ZXh0PgogIDxsaW5lIHgxPSIxMDAiIHkxPSI3MjAiIHgyPSI1MDAiIHkyPSI3MjAiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLW9wYWNpdHk9IjAuMyIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHRleHQgeD0iMzAwIiB5PSI3NzAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjUwMCIgZm9udC1zaXplPSIxOCIgZmlsbD0iI2NiZDVlMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RGFuY2UgcHJhY3RpY2UgZG9uZSwgY2F0IHRpbWUgbm93ITwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjgxMCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjYTg1NWY3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVFJBWSBLSURTIE9GRklDSUFMIFNUT1JZIPCfp608L3RleHQ+Cjwvc3ZnPg==", time: "3h ago" },
            'hyunjin': { title: "Hyunjin (@hynjinnnn)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaHl1bmppbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNEOTc3MDYiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzhCNUNGNiIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2h5dW5qaW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19oeXVuamluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oeXVuamluKSI+SEo8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+lnzwvdGV4dD4KPC9zdmc+", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/wn46oIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzc4MzUwZiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNDUxYTAzIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI5MDAiIGZpbGw9InVybCgjc19ncmFkX/CfjqgpIi8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDgiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIzNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4xMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iMzgwIiBmb250LXNpemU9IjEyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+OqDwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QVJUIENBTlZBUyDwn46oPC90ZXh0PgogIDx0ZXh0IHg9IjMwMCIgeT0iNjkwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjIiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk5ldyBQYWludGluZyBGaW5pc2hlZDwvdGV4dD4KICA8bGluZSB4MT0iMTAwIiB5MT0iNzIwIiB4Mj0iNTAwIiB5Mj0iNzIwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1vcGFjaXR5PSIwLjMiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iNzcwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI1MDAiIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiNjYmQ1ZTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkRyYW1hdGljIGFydCBzZXNzaW9uIGF0IDIgQU0uPC90ZXh0PgogIDx0ZXh0IHg9IjMwMCIgeT0iODEwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI4MDAiIGZvbnQtc2l6ZT0iMTYiIGZpbGw9IiNhODU1ZjciIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNUUkFZIEtJRFMgT0ZGSUNJQUwgU1RPUlkg8J+nrTwvdGV4dD4KPC9zdmc+", time: "4h ago" },
            'han': { title: "Han Jisung (@_doolsetnet)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaGFuIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzI1NjNFQiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDZCNkQ0IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxmaWx0ZXIgaWQ9ImZfaGFuIiB4PSItMjAlIiB5PSItMjAlIiB3aWR0aD0iMTQwJSIgaGVpZ2h0PSIxNDAlIj4KICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iNiIgZmxvb2QtY29sb3I9IiMwMDAiIGZsb29kLW9wYWNpdHk9IjAuNiIvPgogICAgPC9maWx0ZXI+CiAgPC9kZWZzPgogIDxjaXJjbGUgY3g9IjEwMCIgY3k9IjEwMCIgcj0iMTAwIiBmaWxsPSJ1cmwoI2dfaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9oYW4pIj5KUzwvdGV4dD4KICA8dGV4dCB4PSIxMDAiIHk9IjE0MiIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjI4IiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj7wn6aYPC90ZXh0Pgo8L3N2Zz4=", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/imJUiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMWUzYThhIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMxNzI1NTQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8cmVjdCB3aWR0aD0iNjAwIiBoZWlnaHQ9IjkwMCIgZmlsbD0idXJsKCNzX2dyYWRf4piVKSIvPgogIDxjaXJjbGUgY3g9IjMwMCIgY3k9IjM1MCIgcj0iMTgwIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjA4Ii8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxMjAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMTIiLz4KICA8dGV4dCB4PSIzMDAiIHk9IjM4MCIgZm9udC1zaXplPSIxMjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPuKYlTwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U09OR1dSSVRJTkcg8J+OtTwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjY5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjIyIiBmaWxsPSIjZTJlOGYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj4zIFNvbmdzIFdyaXR0ZW4gVG9uaWdodDwvdGV4dD4KICA8bGluZSB4MT0iMTAwIiB5MT0iNzIwIiB4Mj0iNTAwIiB5Mj0iNzIwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1vcGFjaXR5PSIwLjMiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iNzcwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI1MDAiIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiNjYmQ1ZTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkNoZWVzZWNha2UgaW5zcGlyYXRpb24gaGl0IGhhcmQhPC90ZXh0PgogIDx0ZXh0IHg9IjMwMCIgeT0iODEwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI4MDAiIGZvbnQtc2l6ZT0iMTYiIGZpbGw9IiNhODU1ZjciIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNUUkFZIEtJRFMgT0ZGSUNJQUwgU1RPUlkg8J+nrTwvdGV4dD4KPC9zdmc+", time: "5h ago" },
            'changbin': { title: "Changbin (@jutdwae)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbmdiaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjREMyNjI2IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNTlFMEIiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9jaGFuZ2JpbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2NoYW5nYmluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuZ2JpbikiPkNCPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLfwn5CwPC90ZXh0Pgo8L3N2Zz4=", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/wn5KqIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzdmMWQxZCIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNDUwYTBhIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI5MDAiIGZpbGw9InVybCgjc19ncmFkX/CfkqopIi8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDgiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIzNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4xMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iMzgwIiBmb250LXNpemU9IjEyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+SqjwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+SlVUREFFIEdZTSDwn4+L77iP4oCN4pmC77iPPC90ZXh0PgogIDx0ZXh0IHg9IjMwMCIgeT0iNjkwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjIiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkxhdGUgTmlnaHQgQmljZXAgR2FpbnM8L3RleHQ+CiAgPGxpbmUgeDE9IjEwMCIgeTE9IjcyMCIgeDI9IjUwMCIgeTI9IjcyMCIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utb3BhY2l0eT0iMC4zIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSIzMDAiIHk9Ijc3MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNTAwIiBmb250LXNpemU9IjE4IiBmaWxsPSIjY2JkNWUxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5Qcm90ZWluIHNoYWtlIGJyZWFrISBOZXZlciBnaXZlIHVwITwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjgxMCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjYTg1NWY3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVFJBWSBLSURTIE9GRklDSUFMIFNUT1JZIPCfp608L3RleHQ+Cjwvc3ZnPg==", time: "6h ago" },
            'seungmin': { title: "Seungmin (@miniverse.___)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9Imdfc2V1bmdtaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMDI4NEM3IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMzOEJERjgiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9zZXVuZ21pbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX3NldW5nbWluKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9zZXVuZ21pbikiPlNNPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkLY8L3RleHQ+Cjwvc3ZnPg==", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/wn46Z77iPIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzAzNjlhMSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDgyZjQ5IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI5MDAiIGZpbGw9InVybCgjc19ncmFkX/CfjpnvuI8pIi8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDgiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIzNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4xMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iMzgwIiBmb250LXNpemU9IjEyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+Ome+4jzwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Vk9DQUwgQk9PVEgg8J+QtjwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjY5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjIyIiBmaWxsPSIjZTJlOGYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5IaWdoIE5vdGUgV2FybXVwIENvbXBsZXRlPC90ZXh0PgogIDxsaW5lIHgxPSIxMDAiIHkxPSI3MjAiIHgyPSI1MDAiIHkyPSI3MjAiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLW9wYWNpdHk9IjAuMyIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHRleHQgeD0iMzAwIiB5PSI3NzAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjUwMCIgZm9udC1zaXplPSIxOCIgZmlsbD0iI2NiZDVlMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+VGVhc2luZyBDaGFuZ2JpbiBoeXVuZyBhbGwgZGF5LjwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjgxMCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjYTg1NWY3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVFJBWSBLSURTIE9GRklDSUFMIFNUT1JZIPCfp608L3RleHQ+Cjwvc3ZnPg==", time: "7h ago" },
            'in': { title: "I.N (@i.2.n.8)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfaW4iIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRUE1ODBDIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGOTczMTYiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9pbiIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2luKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9pbikiPklOPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfpoo8L3RleHQ+Cjwvc3ZnPg==", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/wn5GUIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzdjMmQxMiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNDMxNDA3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI5MDAiIGZpbGw9InVybCgjc19ncmFkX/CfkZQpIi8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDgiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIzNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4xMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iMzgwIiBmb250LXNpemU9IjEyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+RlDwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+T09URCBTVFlMRSDwn6aKPC90ZXh0PgogIDx0ZXh0IHg9IjMwMCIgeT0iNjkwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjIiIGZpbGw9IiNlMmU4ZjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk1ha25hZSBGYXNoaW9uIEZvciBTY2hlZHVsZTwvdGV4dD4KICA8bGluZSB4MT0iMTAwIiB5MT0iNzIwIiB4Mj0iNTAwIiB5Mj0iNzIwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1vcGFjaXR5PSIwLjMiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iNzcwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI1MDAiIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiNjYmQ1ZTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkh5dW5ncyBib3VnaHQgbWUgZGlubmVyIGFnYWluITwvdGV4dD4KICA8dGV4dCB4PSIzMDAiIHk9IjgxMCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iODAwIiBmb250LXNpemU9IjE2IiBmaWxsPSIjYTg1NWY3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5TVFJBWSBLSURTIE9GRklDSUFMIFNUT1JZIPCfp608L3RleHQ+Cjwvc3ZnPg==", time: "8h ago" },
            'dispatch': { title: "Dispatch Official (@kpop_dispatch)", avatar: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZGlzcGF0Y2giIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMxMTE4MjciIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9kaXNwYXRjaCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2Rpc3BhdGNoKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9kaXNwYXRjaCkiPkQ8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+aqDwvdGV4dD4KPC9zdmc+", img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2MDAiIGhlaWdodD0iOTAwIiB2aWV3Qm94PSIwIDAgNjAwIDkwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNfZ3JhZF/wn5OwIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzQ1MGEwYSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDAwMDAwIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjYwMCIgaGVpZ2h0PSI5MDAiIGZpbGw9InVybCgjc19ncmFkX/Cfk7ApIi8+CiAgPGNpcmNsZSBjeD0iMzAwIiBjeT0iMzUwIiByPSIxODAiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMDgiLz4KICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSIzNTAiIHI9IjEyMCIgZmlsbD0iI2ZmZmZmZiIgb3BhY2l0eT0iMC4xMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iMzgwIiBmb250LXNpemU9IjEyMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+TsDwvdGV4dD4KICA8cmVjdCB4PSI0MCIgeT0iNTgwIiB3aWR0aD0iNTIwIiBoZWlnaHQ9IjI2MCIgcng9IjI0IiBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIwLjY1Ii8+CiAgPHRleHQgeD0iMzAwIiB5PSI2NDAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjkwMCIgZm9udC1zaXplPSIzMiIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RElTUEFUQ0ggRVhDTFVTSVZFIPCfmqg8L3RleHQ+CiAgPHRleHQgeD0iMzAwIiB5PSI2OTAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyMiIgZmlsbD0iI2UyZThmMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+SllQIENlbnRlciBBcnJpdmFsIFBob3RvczwvdGV4dD4KICA8bGluZSB4MT0iMTAwIiB5MT0iNzIwIiB4Mj0iNTAwIiB5Mj0iNzIwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1vcGFjaXR5PSIwLjMiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjMwMCIgeT0iNzcwIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI1MDAiIGZvbnQtc2l6ZT0iMTgiIGZpbGw9IiNjYmQ1ZTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk1hbmFnZXIgQGdhZXJ3ZW5pbGwgc3BvdHRlZCB3aXRoIFNLWiE8L3RleHQ+CiAgPHRleHQgeD0iMzAwIiB5PSI4MTAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIxNiIgZmlsbD0iI2E4NTVmNyIgdGV4dC1hbmNob3I9Im1pZGRsZSI+U1RSQVkgS0lEUyBPRkZJQ0lBTCBTVE9SWSDwn6etPC90ZXh0Pgo8L3N2Zz4=", time: "9h ago" }
        };

        const DM_RESPONSES = {
            'chan': ["I got your message @gaerwenill! I will make sure the rest of the members rest before tomorrow's practice. Thanks for taking care of us! 🐺", "Thanks @gaerwenill! Really appreciate your guidance as always. See you at the studio in 20 minutes!", "Sounds perfect @gaerwenill. Seungmin and Lee Know are just finishing up dinner and we'll head over."],
            'felix': ["Manager @gaerwenill! I saved 3 brownies for you in the break room! Hope you like them! ✨🍪", "Thank you @gaerwenill! I'm practicing my vocal lines right now. See you soon! ❤️", "Yay! Thanks @gaerwenill! Stay warm today!"],
            'leeknow': ["Did Sooni approve this message @gaerwenill? 🐱", "Thanks @gaerwenill. Now please order Korean BBQ for dinner. 🥩", "Dance rehearsal finished. Legs are fine, patience is not. 😏"],
            'hyunjin': ["The aesthetic for tomorrow's photoshoot is so amazing @gaerwenill! 🎨", "Kami bit my sock again 😭 Manager @gaerwenill help me!", "Thank you @gaerwenill! See you at rehearsal!"],
            'han': ["I wrote 2 new songs during lunch break! You're welcome @gaerwenill! 🎵", "Can we order cheesecake for dinner? For musical inspiration obviously. 🍰", "Thanks Manager @gaerwenill!!"],
            'changbin': ["JUTDAE! We do things with conviction @gaerwenill! 💪🔥", "Did you see my bicep gains today Manager?! Protein time!", "3RACHA ready to record! Let's go!"],
            'seungmin': ["Vocal warmup complete @gaerwenill! Ready for comeback recording 🐶", "Changbin hyung is being noisy again Manager...", "Day 1290 of teasing Changbin hyung. Going great."],
            'in': ["Look at my OOTD for today Manager @gaerwenill! 😎", "The hyungs bought me dinner again. Maknae wins! 🥖", "Thanks @gaerwenill! See you soon!"]
        };

        function switchTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            document.getElementById('nav-' + tabName).classList.add('active');
        }

        function uploadProfilePhoto(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(evt) {
                    myAvatarUrl = evt.target.result;
                    document.getElementById('header-my-avatar').src = myAvatarUrl;
                    document.getElementById('story-my-avatar').src = myAvatarUrl;
                    document.getElementById('create-my-avatar').src = myAvatarUrl;
                    document.getElementById('profile-main-avatar').src = myAvatarUrl;
                    STORY_DATA['gaerwenill'].avatar = myAvatarUrl;
                    alert("Profile photo updated successfully!");
                };
                reader.readAsDataURL(file);
            }
        }

        function uploadPostPhoto(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(evt) {
                    currentPostImg = evt.target.result;
                    document.getElementById('post-img-preview').src = currentPostImg;
                    document.getElementById('post-img-preview-container').style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        }

        function removePostImg() {
            currentPostImg = "";
            document.getElementById('post-img-preview').src = "";
            document.getElementById('post-img-preview-container').style.display = 'none';
        }

        function createNewPost() {
            const text = document.getElementById('new-post-text').value.trim();
            if (!text) { alert("Please write something to post!"); return; }
            
            const postId = Date.now();
            let imgHTML = currentPostImg ? `<img src="${currentPostImg}" class="post-image-card">` : '';

            const postHTML = `
                <div class="post" id="post-${postId}">
                    <img src="${myAvatarUrl}" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Gaerwenill</span> <span class="verified-badge">☑️</span>
                            <span class="post-handle">@gaerwenill · Just now</span>
                        </div>
                        <div class="post-text">${text}</div>
                        ${imgHTML}
                        <div class="post-actions">
                            <div class="action-item">💬 <span id="comments-count-${postId}">2</span></div>
                            <div class="action-item">🔄 1,240</div>
                            <div class="action-item" onclick="toggleLike(this, ${postId})">❤️ <span class="like-num">8,420</span></div>
                        </div>
                        <div class="comments-list" id="comments-list-${postId}">
                            <div class="comment-item">
                                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+" class="comment-avatar">
                                <div class="comment-body">
                                    <div class="comment-author">Bang Chan <span class="verified-badge">☑️</span> <span class="comment-handle">@gnabnahc</span></div>
                                    <div class="comment-text">Let's go @gaerwenill! Thanks for taking care of us! 🔥❤️</div>
                                    <button class="comment-reply-btn" onclick="toggleReplyBox('reply-box-${postId}-1')">💬 Reply</button>
                                    <div class="inline-reply-box" id="reply-box-${postId}-1">
                                        <input type="text" class="inline-reply-input" id="reply-input-${postId}-1" placeholder="Reply to @gnabnahc...">
                                        <button class="inline-reply-send" onclick="sendReply(${postId}, 'Bang Chan', '@gnabnahc', 'reply-input-${postId}-1', 'reply-box-${postId}-1')">Send</button>
                                    </div>
                                </div>
                            </div>
                            <div class="comment-item">
                                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfZmVsaXgiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRTExRDQ4IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGNDNGNUUiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGZpbHRlciBpZD0iZl9mZWxpeCIgeD0iLTIwJSIgeT0iLTIwJSIgd2lkdGg9IjE0MCUiIGhlaWdodD0iMTQwJSI+CiAgICAgIDxmZURyb3BTaGFkb3cgZHg9IjAiIGR5PSI0IiBzdGREZXZpYXRpb249IjYiIGZsb29kLWNvbG9yPSIjMDAwIiBmbG9vZC1vcGFjaXR5PSIwLjYiLz4KICAgIDwvZmlsdGVyPgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNnX2ZlbGl4KSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9mZWxpeCkiPkZMPC90ZXh0PgogIDx0ZXh0IHg9IjEwMCIgeT0iMTQyIiBmb250LWZhbWlseT0iLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCBSb2JvdG8sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI3MDAiIGZvbnQtc2l6ZT0iMjgiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfkKU8L3RleHQ+Cjwvc3ZnPg==" class="comment-avatar">
                                <div class="comment-body">
                                    <div class="comment-author">Felix <span class="verified-badge">☑️</span> <span class="comment-handle">@yong.lixx</span></div>
                                    <div class="comment-text">Manager @gaerwenill is the best!! ✨🍪</div>
                                    <button class="comment-reply-btn" onclick="toggleReplyBox('reply-box-${postId}-2')">💬 Reply</button>
                                    <div class="inline-reply-box" id="reply-box-${postId}-2">
                                        <input type="text" class="inline-reply-input" id="reply-input-${postId}-2" placeholder="Reply to @yong.lixx...">
                                        <button class="inline-reply-send" onclick="sendReply(${postId}, 'Felix', '@yong.lixx', 'reply-input-${postId}-2', 'reply-box-${postId}-2')">Send</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;

            document.getElementById('feed-container').insertAdjacentHTML('afterbegin', postHTML);
            document.getElementById('new-post-text').value = '';
            removePostImg();
            alert("Post published successfully!");
        }

        function toggleLike(el, postId) {
            el.classList.toggle('liked');
            let numSpan = el.querySelector('.like-num');
            let text = numSpan.innerText.replace('K', '000').replace(',', '');
            let val = parseInt(text) || 100;
            if (el.classList.contains('liked')) {
                val++;
            } else {
                val--;
            }
            numSpan.innerText = val > 1000 ? (val/1000).toFixed(1) + 'K' : val;
        }

        function toggleReplyBox(boxId) {
            const box = document.getElementById(boxId);
            if (box) {
                box.classList.toggle('active');
            }
        }

        function sendReply(postId, targetName, targetHandle, inputId, boxId) {
            const input = document.getElementById(inputId);
            if (!input || !input.value.trim()) return;
            const text = input.value.trim();

            const commentsList = document.getElementById('comments-list-' + postId);
            const newCommentHTML = `
                <div class="comment-item">
                    <img src="${myAvatarUrl}" class="comment-avatar">
                    <div class="comment-body">
                        <div class="comment-author">Gaerwenill <span class="verified-badge">☑️</span> <span class="comment-handle">@gaerwenill</span></div>
                        <div class="comment-text"><strong>Replying to ${targetHandle}:</strong> ${text}</div>
                    </div>
                </div>
            `;
            commentsList.insertAdjacentHTML('beforeend', newCommentHTML);
            input.value = '';
            toggleReplyBox(boxId);

            // Trigger automated bot reply after 1.5s
            setTimeout(() => {
                const botReplyHTML = `
                    <div class="comment-item">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImdfY2hhbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3OTI4Q0EiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGMDA4MCIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgICA8ZmlsdGVyIGlkPSJmX2NoYW4iIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iNCIgc3RkRGV2aWF0aW9uPSI2IiBmbG9vZC1jb2xvcj0iIzAwMCIgZmxvb2Qtb3BhY2l0eT0iMC42Ii8+CiAgICA8L2ZpbHRlcj4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTAwIiByPSIxMDAiIGZpbGw9InVybCgjZ19jaGFuKSIgLz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSI3MiIgcj0iMzgiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHBhdGggZD0iTSAyOCwxNzggQyAyOCwxMjQgMTcyLDEyNCAxNzIsMTc4IFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMjIiIC8+CiAgPHRleHQgeD0iMTAwIiB5PSI5MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIEJsaW5rTWFjU3lzdGVtRm9udCwgUm9ib3RvLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iOTAwIiBmb250LXNpemU9IjQwIiBmaWxsPSIjZmZmZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWx0ZXI9InVybCgjZl9jaGFuKSI+QkM8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSIxNDIiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBCbGlua01hY1N5c3RlbUZvbnQsIFJvYm90bywgc2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjcwMCIgZm9udC1zaXplPSIyOCIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+8J+QujwvdGV4dD4KPC9zdmc+" class="comment-avatar">
                        <div class="comment-body">
                            <div class="comment-author">Bang Chan <span class="verified-badge">☑️</span> <span class="comment-handle">@gnabnahc</span></div>
                            <div class="comment-text">Got it Manager @gaerwenill! Thanks for the quick feedback! 👍❤️</div>
                        </div>
                    </div>
                `;
                commentsList.insertAdjacentHTML('beforeend', botReplyHTML);
            }, 1500);
        }

        function openStory(key) {
            const data = STORY_DATA[key];
            if (data) {
                document.getElementById('modal-story-avatar').src = data.avatar;
                document.getElementById('modal-story-title').innerText = data.title;
                document.getElementById('modal-story-time').innerText = data.time;
                document.getElementById('modal-story-img').src = data.img;
                
                // Reset timer bar animation
                const timer = document.getElementById('story-timer');
                timer.style.animation = 'none';
                timer.offsetHeight; /* trigger reflow */
                timer.style.animation = 'storyTimer 5s linear forwards';

                document.getElementById('story-modal').classList.add('active');
            }
        }

        function closeStory() {
            document.getElementById('story-modal').classList.remove('active');
        }

        function sendStoryReply() {
            const input = document.getElementById('story-reply-input');
            if (input.value.trim()) {
                alert("Reply sent to story!");
                input.value = '';
                closeStory();
            }
        }

        function selectDMChat(key, name, avatar, handle, el) {
            activeDMKey = key;
            document.querySelectorAll('.dm-member-item').forEach(item => item.classList.remove('active'));
            if (el) el.classList.add('active');

            document.getElementById('dm-active-avatar').src = avatar;
            document.getElementById('dm-active-title').innerHTML = `${name} <span class="verified-badge">☑️</span>`;
            
            const chatBox = document.getElementById('dm-chat-box');
            chatBox.innerHTML = `
                <div class="chat-bubble incoming">
                    <strong>${name} (${handle}):</strong><br>
                    Hey Manager @gaerwenill! Ready for today's schedule. What's our next priority?
                </div>
            `;
        }

        function sendDM() {
            const input = document.getElementById('dm-text-input');
            const text = input.value.trim();
            if (!text) return;

            const chatBox = document.getElementById('dm-chat-box');
            chatBox.innerHTML += `
                <div class="chat-bubble outgoing">
                    <strong>@gaerwenill:</strong><br>${text}
                </div>
            `;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;

            setTimeout(() => {
                const resps = DM_RESPONSES[activeDMKey] || DM_RESPONSES['chan'];
                const randomResp = resps[Math.floor(Math.random() * resps.length)];
                chatBox.innerHTML += `
                    <div class="chat-bubble incoming">
                        ${randomResp}
                    </div>
                `;
                chatBox.scrollTop = chatBox.scrollHeight;
            }, 1200);
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=920, scrolling=True)
