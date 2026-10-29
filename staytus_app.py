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
        .app-container { width: 100%; max-width: 480px; background-color: #000000; min-height: 100vh; border-left: 1px solid #16181c; border-right: 1px solid #16181c; display: flex; flex-direction: column; position: relative; padding-bottom: 70px; }
        
        .top-header { position: sticky; top: 0; background: rgba(0, 0, 0, 0.92); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); z-index: 100; padding: 12px 16px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #16181c; }
        .app-logo { font-size: 20px; font-weight: 900; background: linear-gradient(45deg, #a855f7, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; display: flex; align-items: center; gap: 6px; }
        .header-avatar-btn { width: 38px; height: 38px; border-radius: 50%; border: 2px solid #a855f7; overflow: hidden; cursor: pointer; background: #1f2937; }
        .header-avatar-btn img { width: 100%; height: 100%; object-fit: cover; }

        .stories-container { display: flex; gap: 14px; padding: 14px 16px; overflow-x: auto; border-bottom: 1px solid #16181c; scrollbar-width: none; background: #000000; }
        .stories-container::-webkit-scrollbar { display: none; }
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; flex-shrink: 0; }
        .story-ring { width: 66px; height: 66px; border-radius: 50%; padding: 2px; background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888); display: flex; align-items: center; justify-content: center; }
        .story-avatar { width: 60px; height: 60px; border-radius: 50%; border: 2px solid #000; object-fit: cover; background: #16181c; }
        .story-username { font-size: 11px; color: #71767b; width: 68px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 600; }

        .story-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.96); z-index: 2000; justify-content: center; align-items: center; }
        .story-modal.active { display: flex; }
        .story-modal-content { width: 100%; max-width: 440px; height: 100%; max-height: 820px; background: #000; position: relative; display: flex; flex-direction: column; border-radius: 16px; overflow: hidden; }
        .story-progress-bar { height: 3px; background: rgba(255,255,255,0.3); margin: 12px 12px 6px 12px; border-radius: 2px; overflow: hidden; }
        .story-progress-fill { height: 100%; background: #ffffff; width: 100%; }
        .story-modal-header { display: flex; align-items: center; justify-content: space-between; padding: 6px 16px; z-index: 10; }
        .story-modal-user { display: flex; align-items: center; gap: 10px; }
        .story-modal-avatar { width: 38px; height: 38px; border-radius: 50%; border: 2px solid #a855f7; object-fit: cover; }
        .story-modal-title { font-weight: 700; font-size: 14px; color: #fff; }
        .story-modal-time { font-size: 12px; color: #94a3b8; }
        .story-close-btn { background: none; border: none; color: #fff; font-size: 26px; cursor: pointer; padding: 4px 8px; }
        .story-modal-body { flex: 1; display: flex; justify-content: center; align-items: center; position: relative; overflow: hidden; background: #050505; }
        .story-modal-img { width: 100%; height: 100%; object-fit: cover; }
        .story-caption-overlay { position: absolute; bottom: 20px; left: 16px; right: 16px; background: rgba(0,0,0,0.7); backdrop-filter: blur(8px); padding: 12px 16px; border-radius: 12px; color: #fff; font-size: 14px; font-weight: 500; }
        .story-modal-footer { padding: 12px 16px 20px 16px; background: #000; display: flex; gap: 10px; align-items: center; }
        .story-input { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 20px; padding: 10px 16px; color: #fff; outline: none; font-size: 14px; }
        .story-send-btn { background: #a855f7; color: #fff; border: none; padding: 10px 18px; border-radius: 20px; font-weight: 700; cursor: pointer; }

        .tab-content { display: none; }
        .tab-content.active { display: block; }

        .create-post-box { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .create-post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; border: 2px solid #a855f7; }
        .create-post-input-area { flex: 1; display: flex; flex-direction: column; gap: 10px; }
        .create-post-textarea { width: 100%; background: transparent; border: none; color: #f7f9f9; outline: none; font-size: 15px; resize: none; min-height: 50px; }
        .image-preview-container { display: none; position: relative; margin-top: 8px; border-radius: 12px; overflow: hidden; max-height: 200px; border: 1px solid #2f3336; }
        .image-preview-container img { width: 100%; height: 100%; object-fit: cover; }
        .remove-img-btn { position: absolute; top: 8px; right: 8px; background: rgba(0,0,0,0.7); color: #fff; border: none; border-radius: 50%; width: 26px; height: 26px; cursor: pointer; font-weight: bold; }
        .create-post-actions { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #16181c; padding-top: 10px; }
        .attach-file-label { background: #1e293b; color: #a855f7; border: 1px solid #334155; padding: 6px 14px; border-radius: 18px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 6px; }
        .post-submit-btn { background: #a855f7; color: white; border: none; padding: 8px 20px; border-radius: 20px; font-weight: 700; cursor: pointer; font-size: 14px; }

        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000; }
        .post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #16181c; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 4px; margin-bottom: 4px; flex-wrap: wrap; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 13px; }
        .post-handle { color: #71767b; font-size: 14px; }
        .post-text { font-size: 15px; line-height: 1.4; color: #e7e9ea; margin-bottom: 10px; white-space: pre-wrap; }
        .post-image-card { width: 100%; border-radius: 16px; margin-bottom: 10px; border: 1px solid #2f3336; object-fit: cover; max-height: 340px; }

        .post-actions { display: flex; justify-content: space-between; max-width: 360px; color: #71767b; font-size: 13px; margin-top: 8px; }
        .action-item { display: flex; align-items: center; gap: 6px; cursor: pointer; padding: 4px; transition: color 0.2s; }
        .action-item:hover { color: #a855f7; }
        .action-item.liked { color: #f91880; font-weight: bold; }

        .comments-list { margin-top: 12px; border-top: 1px solid #16181c; padding-top: 10px; display: flex; flex-direction: column; gap: 10px; }
        .comment-item { display: flex; gap: 10px; background: #090d14; padding: 10px 12px; border-radius: 12px; border: 1px solid #1e293b; }
        .comment-avatar { width: 34px; height: 34px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
        .comment-body { flex: 1; }
        .comment-author-row { display: flex; align-items: center; gap: 6px; }
        .comment-author { font-weight: 700; font-size: 13px; color: #f7f9f9; }
        .comment-handle { color: #64748b; font-size: 12px; }
        .comment-text { font-size: 13px; color: #cbd5e1; margin-top: 3px; line-height: 1.35; }
        .comment-reply-btn { background: none; border: none; color: #a855f7; font-size: 12px; font-weight: 700; cursor: pointer; margin-top: 5px; display: inline-block; }
        .inline-reply-box { display: none; margin-top: 8px; gap: 8px; }
        .inline-reply-box.active { display: flex; }
        .inline-reply-input { flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 16px; padding: 6px 12px; color: #fff; font-size: 12px; outline: none; }
        .inline-reply-send { background: #a855f7; color: #fff; border: none; padding: 6px 14px; border-radius: 16px; font-size: 12px; font-weight: 700; cursor: pointer; }

        .dm-layout { display: flex; height: calc(100vh - 135px); background: #000; }
        .dm-sidebar { width: 115px; border-right: 1px solid #16181c; display: flex; flex-direction: column; overflow-y: auto; background: #000; scrollbar-width: none; }
        .dm-sidebar::-webkit-scrollbar { display: none; }
        .dm-member-item { padding: 12px 6px; display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; border-bottom: 1px solid #16181c; text-align: center; opacity: 0.65; transition: 0.2s; }
        .dm-member-item.active { opacity: 1; background: #111827; border-left: 3px solid #a855f7; }
        .dm-member-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 1px solid #334155; }
        .dm-member-name { font-size: 11px; font-weight: 700; color: #e2e8f0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 95px; }

        .dm-chat-area { flex: 1; display: flex; flex-direction: column; background: #000; }
        .dm-chat-header { padding: 12px 16px; border-bottom: 1px solid #16181c; display: flex; align-items: center; gap: 10px; background: #090d16; }
        .dm-chat-avatar { width: 38px; height: 38px; border-radius: 50%; object-fit: cover; border: 2px solid #a855f7; }
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
        .profile-banner { width: 100%; height: 140px; object-fit: cover; background: #1e293b; }
        .profile-header { padding: 0 16px 16px 16px; position: relative; display: flex; flex-direction: column; border-bottom: 1px solid #16181c; }
        .profile-avatar-wrapper { position: relative; width: 88px; height: 88px; margin-top: -44px; margin-bottom: 10px; }
        .profile-avatar { width: 88px; height: 88px; border-radius: 50%; border: 4px solid #000; object-fit: cover; background: #1e293b; }
        .profile-cam-btn { position: absolute; bottom: 2px; right: 2px; background: #a855f7; color: #fff; border: 2px solid #000; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; cursor: pointer; }
        .profile-name { font-size: 20px; font-weight: 900; color: #fff; display: flex; align-items: center; gap: 6px; }
        .profile-handle { color: #64748b; font-size: 14px; margin-bottom: 8px; }
        .profile-bio { font-size: 14px; color: #e2e8f0; line-height: 1.4; margin-bottom: 12px; }
        .profile-stats { display: flex; gap: 20px; font-size: 14px; color: #94a3b8; }
        .profile-stat-num { font-weight: 800; color: #fff; }

        .search-container { padding: 16px; background: #000; }
        .search-bar-input { width: 100%; background: #1e293b; border: 1px solid #334155; border-radius: 20px; padding: 12px 18px; color: #fff; font-size: 14px; outline: none; margin-bottom: 16px; }
        .trend-card { background: #090d16; border: 1px solid #1e293b; padding: 14px; border-radius: 12px; margin-bottom: 10px; }
        .trend-category { font-size: 12px; color: #64748b; }
        .trend-tag { font-size: 15px; font-weight: 800; color: #fff; margin: 2px 0; }
        .trend-posts { font-size: 12px; color: #94a3b8; }

        .bottom-nav { position: fixed; bottom: 0; width: 100%; max-width: 480px; background: rgba(0, 0, 0, 0.94); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-top: 1px solid #16181c; display: flex; justify-content: space-around; padding: 10px 0; z-index: 1000; }
        .nav-item { color: #64748b; font-size: 12px; text-decoration: none; cursor: pointer; font-weight: 700; display: flex; flex-direction: column; align-items: center; gap: 3px; transition: 0.2s; }
        .nav-item.active { color: #a855f7; }
        .nav-icon { font-size: 18px; }
    </style>
</head>
<body>
<div class="app-container">
    <div class="top-header">
        <div class="app-logo"><span>🧭</span> Status AI</div>
        <div class="header-avatar-btn" onclick="switchTab('profile')">
            <img id="topHeaderAvatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzkzMzNlYSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZWM0ODk5IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMTExODI3IiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNhODU1ZjciIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjYTg1NWY3IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTIsODUgQyA0OCwzMCAxNTIsMzAgMTQ4LDg1IEMgMTUyLDExNSAxNDIsMTM1IDEzOCwxNDAgQyAxMzUsMTEwIDEzOCw3MCAxMzUsNjAgQyAxMjAsNDAgODAsNDAgNjUsNjAgQyA2Miw3MCA2NSwxMTAgNjIsMTQwIEMgNTgsMTM1IDQ4LDExNSA1Miw4NSBaIiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIDxyZWN0IHg9IjU4IiB5PSI2MiIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjgiIHJ4PSI0IiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIAogIAo8L3N2Zz4=" alt="Manager">
        </div>
    </div>
    <div class="stories-container" id="storiesBar"></div>
    <div class="story-modal" id="storyModal">
        <div class="story-modal-content">
            <div class="story-progress-bar"><div class="story-progress-fill" id="storyProgress"></div></div>
            <div class="story-modal-header">
                <div class="story-modal-user">
                    <img id="storyModalAvatar" class="story-modal-avatar" src="" alt="">
                    <div>
                        <div class="story-modal-title" id="storyModalTitle">Bang Chan</div>
                        <div class="story-modal-time" id="storyModalTime">10m ago</div>
                    </div>
                </div>
                <button class="story-close-btn" onclick="closeStory()">✕</button>
            </div>
            <div class="story-modal-body">
                <img id="storyModalImg" class="story-modal-img" src="" alt="Story">
                <div class="story-caption-overlay" id="storyModalCaption">Late night studio producing... 🎧</div>
            </div>
            <div class="story-modal-footer">
                <input type="text" id="storyReplyInput" class="story-input" placeholder="Reply to story...">
                <button class="story-send-btn" onclick="sendStoryReply()">Send</button>
            </div>
        </div>
    </div>
    <div id="tab-feed" class="tab-content active">
        <div class="create-post-box">
            <img id="createPostUserAvatar" class="create-post-avatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzkzMzNlYSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZWM0ODk5IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMTExODI3IiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNhODU1ZjciIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjYTg1NWY3IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTIsODUgQyA0OCwzMCAxNTIsMzAgMTQ4LDg1IEMgMTUyLDExNSAxNDIsMTM1IDEzOCwxNDAgQyAxMzUsMTEwIDEzOCw3MCAxMzUsNjAgQyAxMjAsNDAgODAsNDAgNjUsNjAgQyA2Miw3MCA2NSwxMTAgNjIsMTQwIEMgNTgsMTM1IDQ4LDExNSA1Miw4NSBaIiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIDxyZWN0IHg9IjU4IiB5PSI2MiIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjgiIHJ4PSI0IiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIAogIAo8L3N2Zz4=" alt="Manager">
            <div class="create-post-input-area">
                <textarea id="newPostText" class="create-post-textarea" placeholder="Post update for STAYs as Manager @gaerwenill..."></textarea>
                <div class="image-preview-container" id="imagePreviewBox">
                    <img id="previewImgTag" src="" alt="Preview">
                    <button class="remove-img-btn" onclick="removeAttachedImg()">✕</button>
                </div>
                <div class="create-post-actions">
                    <label class="attach-file-label">
                        <span>📷</span> Add Photo
                        <input type="file" id="postImgInput" accept="image/*" style="display:none;" onchange="handleImgAttach(event)">
                    </label>
                    <button class="post-submit-btn" onclick="publishNewPost()">🚀 Post</button>
                </div>
            </div>
        </div>
        <div id="feedPosts"></div>
    </div>
    <div id="tab-search" class="tab-content">
        <div class="search-container">
            <input type="text" class="search-bar-input" placeholder="🔍 Search Stray Kids, STAYs, or trends...">
            <h3 style="margin-bottom: 12px; font-size: 16px; color: #a855f7;">Trending Worldwide</h3>
            <div class="trend-card"><div class="trend-category">K-Pop • Trending</div><div class="trend-tag">#StrayKidsWorldTour2026</div><div class="trend-posts">1.4M Posts</div></div>
            <div class="trend-card"><div class="trend-category">Entertainment • Trending</div><div class="trend-tag">#ManagerGaerwenill</div><div class="trend-posts">850K Posts</div></div>
            <div class="trend-card"><div class="trend-category">Music • Trending</div><div class="trend-tag">#3RACHA_NewAlbum</div><div class="trend-posts">620K Posts</div></div>
            <div class="trend-card"><div class="trend-category">K-Pop • Trending</div><div class="trend-tag">#FelixBrowniesRecipe</div><div class="trend-posts">410K Posts</div></div>
        </div>
    </div>
    <div id="tab-dms" class="tab-content">
        <div class="dm-layout">
            <div class="dm-sidebar" id="dmSidebar"></div>
            <div class="dm-chat-area">
                <div class="dm-chat-header">
                    <img id="dmActiveAvatar" class="dm-chat-avatar" src="" alt="">
                    <div>
                        <div id="dmActiveTitle" class="dm-chat-title">Bang Chan</div>
                        <div class="dm-chat-status">● Active Now</div>
                    </div>
                </div>
                <div class="dm-chat-messages" id="dmChatMessages"></div>
                <div class="dm-input-bar">
                    <input type="text" id="dmInputText" class="dm-input" placeholder="Message...">
                    <button class="dm-send-btn" onclick="sendDM()">Send</button>
                </div>
            </div>
        </div>
    </div>
    <div id="tab-profile" class="tab-content">
        <div class="profile-container">
            <img class="profile-banner" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNTAwIiB3aWR0aD0iODAwIiBoZWlnaHQ9IjUwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNreSIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjEiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMDkwNTE0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjUwJSIgc3RvcC1jb2xvcj0iIzJhMDg0NSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNjQxMzcyIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI1MDAiIGZpbGw9InVybCgjc2t5KSIgLz4KICA8IS0tIFN0YWdlIExpZ2h0cyBSYXlzIC0tPgogIDxwb2x5Z29uIHBvaW50cz0iMTAwLDAgMjUwLDUwMCAwLDUwMCIgZmlsbD0iI2E4NTVmNyIgb3BhY2l0eT0iMC4zNSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjMwMCwwIDQwMCw1MDAgMjAwLDUwMCIgZmlsbD0iI2VjNDg5OSIgb3BhY2l0eT0iMC40IiAvPgogIDxwb2x5Z29uIHBvaW50cz0iNTAwLDAgNjAwLDUwMCA0MDAsNTAwIiBmaWxsPSIjM2I4MmY2IiBvcGFjaXR5PSIwLjQiIC8+CiAgPHBvbHlnb24gcG9pbnRzPSI3MDAsMCA4MDAsNTAwIDU1MCw1MDAiIGZpbGw9IiNhODU1ZjciIG9wYWNpdHk9IjAuMzUiIC8+CiAgPCEtLSBDb25jZXJ0IFN0YWdlIFNpbGhvdWV0dGUgLS0+CiAgPHJlY3QgeD0iMCIgeT0iMzgwIiB3aWR0aD0iODAwIiBoZWlnaHQ9IjEyMCIgZmlsbD0iIzAzMDIwNyIgLz4KICA8IS0tIEJhbmQgU2lsaG91ZXR0ZXMgb24gU3RhZ2UgLS0+CiAgPGNpcmNsZSBjeD0iMTgwIiBjeT0iMzQwIiByPSIxNCIgZmlsbD0iIzAwMCIgLz48cGF0aCBkPSJNIDE2NSwzODAgTCAxOTUsMzgwIEwgMTg4LDM1NCBMIDE3MiwzNTQgWiIgZmlsbD0iIzAwMCIgLz4KICA8Y2lyY2xlIGN4PSIyNTAiIGN5PSIzMzUiIHI9IjE0IiBmaWxsPSIjMDAwIiAvPjxwYXRoIGQ9Ik0gMjM1LDM4MCBMIDI2NSwzODAgTCAyNTgsMzQ5IEwgMjQyLDM0OSBaIiBmaWxsPSIjMDAwIiAvPgogIDxjaXJjbGUgY3g9IjMyMCIgY3k9IjMzMCIgcj0iMTUiIGZpbGw9IiMwMDAiIC8+PHBhdGggZD0iTSAzMDUsMzgwIEwgMzM1LDM4MCBMIDMyOCwzNDQgTCAzMTIsMzQ0IFoiIGZpbGw9IiMwMDAiIC8+CiAgPGNpcmNsZSBjeD0iNDAwIiBjeT0iMzI1IiByPSIxNiIgZmlsbD0iIzAwMCIgLz48cGF0aCBkPSJNIDM4MywzODAgTCA0MTcsMzgwIEwgNDEwLDM0MCBMIDM5MCwzNDAgWiIgZmlsbD0iIzAwMCIgLz4KICA8Y2lyY2xlIGN4PSI0ODAiIGN5PSIzMzAiIHI9IjE1IiBmaWxsPSIjMDAwIiAvPjxwYXRoIGQ9Ik0gNDY1LDM4MCBMIDQ5NSwzODAgTCA0ODgsMzQ0IEwgNDcyLDM0NCBaIiBmaWxsPSIjMDAwIiAvPgogIDxjaXJjbGUgY3g9IjU1MCIgY3k9IjMzNSIgcj0iMTQiIGZpbGw9IiMwMDAiIC8+PHBhdGggZD0iTSA1MzUsMzgwIEwgNTY1LDM4MCBMIDU1OCwzNDkgTCA1NDIsMzQ5IFoiIGZpbGw9IiMwMDAiIC8+CiAgPGNpcmNsZSBjeD0iNjIwIiBjeT0iMzQwIiByPSIxNCIgZmlsbD0iIzAwMCIgLz48cGF0aCBkPSJNIDYwNSwzODAgTCA2MzUsMzgwIEwgNjI4LDM1NCBMIDYxMiwzNTQgWiIgZmlsbD0iIzAwMCIgLz4KICA8IS0tIEdsb3dpbmcgTGlnaHRzdGlja3MgaW4gQ3Jvd2QgLS0+CiAgPGNpcmNsZSBjeD0iMTIwIiBjeT0iNDQwIiByPSI0IiBmaWxsPSIjZTBlN2ZmIiAvPgogIDxjaXJjbGUgY3g9IjIyMCIgY3k9IjQ2MCIgcj0iNSIgZmlsbD0iI2MwODRmYyIgLz4KICA8Y2lyY2xlIGN4PSIzNDAiIGN5PSI0MzAiIHI9IjQiIGZpbGw9IiNmNDcyYjYiIC8+CiAgPGNpcmNsZSBjeD0iNDUwIiBjeT0iNDUwIiByPSI1IiBmaWxsPSIjNjBhNWZhIiAvPgogIDxjaXJjbGUgY3g9IjU4MCIgY3k9IjQzNSIgcj0iNCIgZmlsbD0iI2MwODRmYyIgLz4KICA8Y2lyY2xlIGN4PSI2ODAiIGN5PSI0NjAiIHI9IjUiIGZpbGw9IiNlMGU3ZmYiIC8+CiAgPCEtLSBCYW5uZXIgVGV4dCAtLT4KICA8dGV4dCB4PSI0MDAiIHk9IjE2MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iNDQiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSI0Ij5TVFJBWSBLSURTIFdPUkxEIFRPVVI8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyMTAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjI0IiBmaWxsPSIjZWM0ODk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iNiI+RE9NSU5BVEUgMjAyNiDigKIgT0ZGSUNJQUwgREFURVM8L3RleHQ+Cjwvc3ZnPg==" alt="Banner">
            <div class="profile-header">
                <div class="profile-avatar-wrapper">
                    <img id="profileAvatarImg" class="profile-avatar" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzkzMzNlYSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZWM0ODk5IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMTExODI3IiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNhODU1ZjciIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjYTg1NWY3IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTIsODUgQyA0OCwzMCAxNTIsMzAgMTQ4LDg1IEMgMTUyLDExNSAxNDIsMTM1IDEzOCwxNDAgQyAxMzUsMTEwIDEzOCw3MCAxMzUsNjAgQyAxMjAsNDAgODAsNDAgNjUsNjAgQyA2Miw3MCA2NSwxMTAgNjIsMTQwIEMgNTgsMTM1IDQ4LDExNSA1Miw4NSBaIiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIDxyZWN0IHg9IjU4IiB5PSI2MiIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjgiIHJ4PSI0IiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIAogIAo8L3N2Zz4=" alt="Avatar">
                    <label class="profile-cam-btn">
                        📷
                        <input type="file" accept="image/*" style="display:none;" onchange="handleProfilePicChange(event)">
                    </label>
                </div>
                <div class="profile-name">Gaerwenill <span style="color:#1d9bf0;">✔</span></div>
                <div class="profile-handle">@gaerwenill • Head Manager @ JYPE</div>
                <div class="profile-bio">Official Manager for Stray Kids (스트레이 키즈). Managing schedules, comeback teasers, and world tours for STAYs worldwide! 🧭✨</div>
                <div class="profile-stats">
                    <div><span class="profile-stat-num">8</span> Members Managed</div>
                    <div><span class="profile-stat-num">12.8M</span> Followers</div>
                </div>
            </div>
            <h4 style="padding: 14px 16px 8px 16px; color: #a855f7;">Your Manager Updates</h4>
            <div id="profileUserPosts"></div>
        </div>
    </div>
    <div class="bottom-nav">
        <div class="nav-item active" id="nav-feed" onclick="switchTab('feed')"><div class="nav-icon">🏠</div><div>Feed</div></div>
        <div class="nav-item" id="nav-search" onclick="switchTab('search')"><div class="nav-icon">🔍</div><div>Search</div></div>
        <div class="nav-item" id="nav-dms" onclick="switchTab('dms')"><div class="nav-icon">💬</div><div>DMs</div></div>
        <div class="nav-item" id="nav-profile" onclick="switchTab('profile')"><div class="nav-icon">👤</div><div>Profile</div></div>
    </div>
</div>
<script>
    const AVATARS = {
        gaerwenill: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzkzMzNlYSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZWM0ODk5IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMTExODI3IiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNhODU1ZjciIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjYTg1NWY3IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTIsODUgQyA0OCwzMCAxNTIsMzAgMTQ4LDg1IEMgMTUyLDExNSAxNDIsMTM1IDEzOCwxNDAgQyAxMzUsMTEwIDEzOCw3MCAxMzUsNjAgQyAxMjAsNDAgODAsNDAgNjUsNjAgQyA2Miw3MCA2NSwxMTAgNjIsMTQwIEMgNTgsMTM1IDQ4LDExNSA1Miw4NSBaIiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIDxyZWN0IHg9IjU4IiB5PSI2MiIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjgiIHJ4PSI0IiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIAogIAo8L3N2Zz4=",
        bangchan: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzdlMjJjZSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjZGIyNzc3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMGYxNzJhIiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNlYWIzMDgiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjZWFiMzA4IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTYsODIgQyA1MCwzNSAxNTAsMzUgMTQ0LDgyIEMgMTMyLDQ4IDY4LDQ4IDU2LDgyIFoiIGZpbGw9IiNlYWIzMDgiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2Miw3NSBRIDgyLDUwIDEwMCw3MiBRIDExOCw1MCAxMzgsNzUgUSAxMjAsNDIgODAsNDIgUSA2NSw1NSA2Miw3NSBaIiBmaWxsPSIjZmVmMDhhIiAvPgogICAgICAgIAogIAo8L3N2Zz4=",
        leeknow: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzBkOTQ4OCIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDI4NGM3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMWUyOTNiIiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiMzZjIzMTQiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjM2YyMzE0IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTgsODAgQyA1NSwzOCAxNDUsMzggMTQyLDgwIEMgMTMwLDUyIDcwLDUyIDU4LDgwIFoiIGZpbGw9IiMzZjIzMTQiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2MCw3NiBDIDc1LDU2IDk1LDY0IDEwMiw3NCBDIDEwOCw2NCAxMjgsNTYgMTQwLDc2IFEgMTAwLDQ4IDYwLDc2IFoiIGZpbGw9IiM1MjUyNWIiIC8+CiAgICAgICAgCiAgCjwvc3ZnPg==",
        changbin: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2I5MWMxYyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjN2MyZDEyIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMDkwOTBiIiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiMxODE4MWIiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjMTgxODFiIiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTgsODAgQyA1Niw0MCAxNDQsNDAgMTQyLDgwIEMgMTMwLDUyIDcwLDUyIDU4LDgwIFoiIGZpbGw9IiMxODE4MWIiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2MCw3NiBRIDgwLDU1IDEwMCw3MiBRIDEyMCw1NSAxNDAsNzYgUSAxMDAsNDggNjAsNzYgWiIgZmlsbD0iIzE4MTgxYiIgLz4KICAgICAgICAKICA8cGF0aCBkPSJNIDU4LDcyIEMgNTgsNDAgMTQyLDQwIDE0Miw3MiBaIiBmaWxsPSIjMjcyNzJhIiAvPjxyZWN0IHg9IjU0IiB5PSI2OCIgd2lkdGg9IjkyIiBoZWlnaHQ9IjEyIiByeD0iNCIgZmlsbD0iIzNmM2Y0NiIgLz4KPC9zdmc+",
        hyunjin: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzZiMjFhOCIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjYzAyNmQzIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMWUxYjRiIiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNmZWYwOGEiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjZmVmMDhhIiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTIsODUgQyA0OCwzMCAxNTIsMzAgMTQ4LDg1IEMgMTUyLDExNSAxNDIsMTM1IDEzOCwxNDAgQyAxMzUsMTEwIDEzOCw3MCAxMzUsNjAgQyAxMjAsNDAgODAsNDAgNjUsNjAgQyA2Miw3MCA2NSwxMTAgNjIsMTQwIEMgNTgsMTM1IDQ4LDExNSA1Miw4NSBaIiBmaWxsPSIjZmVmMDhhIiAvPgogICAgICAgIDxyZWN0IHg9IjU4IiB5PSI2MiIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjgiIHJ4PSI0IiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIAogIAo8L3N2Zz4=",
        han: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2Q5NzcwNiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNzgzNTBmIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMzM0MTU1IiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiM0NTFhMDMiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjNDUxYTAzIiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTgsODAgQyA1Niw0MCAxNDQsNDAgMTQyLDgwIEMgMTMwLDUyIDcwLDUyIDU4LDgwIFoiIGZpbGw9IiM0NTFhMDMiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2MCw3NiBRIDgwLDU1IDEwMCw3MiBRIDEyMCw1NSAxNDAsNzYgUSAxMDAsNDggNjAsNzYgWiIgZmlsbD0iIzQ1MWEwMyIgLz4KICAgICAgICAKICA8cGF0aCBkPSJNIDYwLDcwIEMgNjAsNDUgMTQwLDQ1IDE0MCw3MCBaIiBmaWxsPSIjMTgxODFiIiAvPjxwYXRoIGQ9Ik0gNDUsNzAgUSAxMDAsNjAgMTU1LDcwIEwgMTUwLDc4IFEgMTAwLDY4IDUwLDc4IFoiIGZpbGw9IiMyNzI3MmEiIC8+Cjwvc3ZnPg==",
        felix: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2JlMTIzYyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjODgxMzM3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMDI4NGM3IiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNmYWNjMTUiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjZmFjYzE1IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTYsODIgQyA1MCwzNSAxNTAsMzUgMTQ0LDgyIEMgMTMyLDQ4IDY4LDQ4IDU2LDgyIFoiIGZpbGw9IiNmYWNjMTUiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2Miw3NSBRIDgyLDUwIDEwMCw3MiBRIDExOCw1MCAxMzgsNzUgUSAxMjAsNDIgODAsNDIgUSA2NSw1NSA2Miw3NSBaIiBmaWxsPSIjZmVmMDhhIiAvPgogICAgICAgIAogIAo8L3N2Zz4=",
        seungmin: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzI1NjNlYiIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMWUzYThhIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMTgxODFiIiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiMyNzI3MmEiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjMjcyNzJhIiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTgsODAgQyA1NSwzOCAxNDUsMzggMTQyLDgwIEMgMTMwLDUyIDcwLDUyIDU4LDgwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2MCw3NiBDIDc1LDU2IDk1LDY0IDEwMiw3NCBDIDEwOCw2NCAxMjgsNTYgMTQwLDc2IFEgMTAwLDQ4IDYwLDc2IFoiIGZpbGw9IiM1MjUyNWIiIC8+CiAgICAgICAgCiAgCjwvc3ZnPg==",
        in: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzA1OTY2OSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMDQ3ODU3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMzEyZTgxIiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiMxODE4MWIiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjMTgxODFiIiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTgsODAgQyA1Niw0MCAxNDQsNDAgMTQyLDgwIEMgMTMwLDUyIDcwLDUyIDU4LDgwIFoiIGZpbGw9IiMxODE4MWIiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2MCw3NiBRIDgwLDU1IDEwMCw3MiBRIDEyMCw1NSAxNDAsNzYgUSAxMDAsNDggNjAsNzYgWiIgZmlsbD0iIzE4MTgxYiIgLz4KICAgICAgICAKICAKPC9zdmc+",
        dispatch: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzExMTgyNyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMzc0MTUxIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMDAwMDAwIiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNlZjQ0NDQiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjZWY0NDQ0IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTgsODAgQyA1NSwzOCAxNDUsMzggMTQyLDgwIEMgMTMwLDUyIDcwLDUyIDU4LDgwIFoiIGZpbGw9IiNlZjQ0NDQiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2MCw3NiBDIDc1LDU2IDk1LDY0IDEwMiw3NCBDIDEwOCw2NCAxMjgsNTYgMTQwLDc2IFEgMTAwLDQ4IDYwLDc2IFoiIGZpbGw9IiM1MjUyNWIiIC8+CiAgICAgICAgCiAgCjwvc3ZnPg==",
        stay1: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2Y0M2Y1ZSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjODgxMzM3IiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjNGMwNTE5IiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiNlYzQ4OTkiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjZWM0ODk5IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTIsODUgQyA0OCwzMCAxNTIsMzAgMTQ4LDg1IEMgMTUyLDExNSAxNDIsMTM1IDEzOCwxNDAgQyAxMzUsMTEwIDEzOCw3MCAxMzUsNjAgQyAxMjAsNDAgODAsNDAgNjUsNjAgQyA2Miw3MCA2NSwxMTAgNjIsMTQwIEMgNTgsMTM1IDQ4LDExNSA1Miw4NSBaIiBmaWxsPSIjZWM0ODk5IiAvPgogICAgICAgIDxyZWN0IHg9IjU4IiB5PSI2MiIgd2lkdGg9Ijg0IiBoZWlnaHQ9IjgiIHJ4PSI0IiBmaWxsPSIjYTg1NWY3IiAvPgogICAgICAgIAogIAo8L3N2Zz4=",
        stay2: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMDAgMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzAyODRjNyIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMWUzYThhIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0ic2tpbiIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZmZkZmM0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmMGMwOWQiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0idXJsKCNiZykiIC8+CiAgPCEtLSBCb2R5IC0tPgogIDxwYXRoIGQ9Ik0gMjgsMjAwIEMgMjgsMTM4IDE3MiwxMzggMTcyLDIwMCBaIiBmaWxsPSIjMGYxNzJhIiAvPgogIDxwYXRoIGQ9Ik0gNjgsMTQ4IEwgMTAwLDE4NiBMIDEzMiwxNDggWiIgZmlsbD0iI2ZmZGZjNCIgLz4KICA8cGF0aCBkPSJNIDY0LDE0MCBMIDEwMCwxNzYgTCAxMzYsMTQwIFoiIGZpbGw9IiMyNzI3MmEiIC8+CiAgPCEtLSBOZWNrIC0tPgogIDxyZWN0IHg9Ijg1IiB5PSIxMDgiIHdpZHRoPSIzMCIgaGVpZ2h0PSIzOCIgcng9IjYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBIZWFkIC0tPgogIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSI5MiIgcng9IjM4IiByeT0iNDYiIGZpbGw9InVybCgjc2tpbikiIC8+CiAgPCEtLSBFYXJzIC0tPgogIDxjaXJjbGUgY3g9IjYyIiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPGNpcmNsZSBjeD0iMTM4IiBjeT0iOTUiIHI9IjkiIGZpbGw9IiNmMGMwOWQiIC8+CiAgPCEtLSBFeWVzIC0tPgogIDxlbGxpcHNlIGN4PSI4MyIgY3k9IjkwIiByeD0iNSIgcnk9IjMuNSIgZmlsbD0iIzE4MTgxYiIgLz4KICA8ZWxsaXBzZSBjeD0iMTE3IiBjeT0iOTAiIHJ4PSI1IiByeT0iMy41IiBmaWxsPSIjMTgxODFiIiAvPgogIDxjaXJjbGUgY3g9Ijg0IiBjeT0iODkiIHI9IjEuNSIgZmlsbD0iI2ZmZmZmZiIgLz4KICA8Y2lyY2xlIGN4PSIxMTgiIGN5PSI4OSIgcj0iMS41IiBmaWxsPSIjZmZmZmZmIiAvPgogIDwhLS0gRXllYnJvd3MgLS0+CiAgPHBhdGggZD0iTSA3NSw4MSBRIDgzLDc3IDkxLDgyIiBzdHJva2U9IiMzYjgyZjYiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIDxwYXRoIGQ9Ik0gMTA5LDgyIFEgMTE3LDc3IDEyNSw4MSIgc3Ryb2tlPSIjM2I4MmY2IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgLz4KICA8IS0tIE5vc2UgJiBNb3V0aCAtLT4KICA8cGF0aCBkPSJNIDEwMCw5MSBMIDk4LDEwMiBMIDEwMywxMDMiIHN0cm9rZT0iI2UwYTA3YSIgc3Ryb2tlLXdpZHRoPSIyIiBmaWxsPSJub25lIiAvPgogIDxwYXRoIGQ9Ik0gOTAsMTE2IFEgMTAwLDEyNCAxMTAsMTE2IiBzdHJva2U9IiNkMDcwNjAiIHN0cm9rZS13aWR0aD0iMyIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiAvPgogIAogICAgICAgIDxwYXRoIGQ9Ik0gNTYsODIgQyA1MCwzNSAxNTAsMzUgMTQ0LDgyIEMgMTMyLDQ4IDY4LDQ4IDU2LDgyIFoiIGZpbGw9IiMzYjgyZjYiIC8+CiAgICAgICAgPHBhdGggZD0iTSA2Miw3NSBRIDgyLDUwIDEwMCw3MiBRIDExOCw1MCAxMzgsNzUgUSAxMjAsNDIgODAsNDIgUSA2NSw1NSA2Miw3NSBaIiBmaWxsPSIjZmVmMDhhIiAvPgogICAgICAgIAogIAo8L3N2Zz4="
    };
    const PHOTOS = {
        concert: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNTAwIiB3aWR0aD0iODAwIiBoZWlnaHQ9IjUwMCI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InNreSIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjEiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMDkwNTE0IiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjUwJSIgc3RvcC1jb2xvcj0iIzJhMDg0NSIgLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNjQxMzcyIiAvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI1MDAiIGZpbGw9InVybCgjc2t5KSIgLz4KICA8IS0tIFN0YWdlIExpZ2h0cyBSYXlzIC0tPgogIDxwb2x5Z29uIHBvaW50cz0iMTAwLDAgMjUwLDUwMCAwLDUwMCIgZmlsbD0iI2E4NTVmNyIgb3BhY2l0eT0iMC4zNSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjMwMCwwIDQwMCw1MDAgMjAwLDUwMCIgZmlsbD0iI2VjNDg5OSIgb3BhY2l0eT0iMC40IiAvPgogIDxwb2x5Z29uIHBvaW50cz0iNTAwLDAgNjAwLDUwMCA0MDAsNTAwIiBmaWxsPSIjM2I4MmY2IiBvcGFjaXR5PSIwLjQiIC8+CiAgPHBvbHlnb24gcG9pbnRzPSI3MDAsMCA4MDAsNTAwIDU1MCw1MDAiIGZpbGw9IiNhODU1ZjciIG9wYWNpdHk9IjAuMzUiIC8+CiAgPCEtLSBDb25jZXJ0IFN0YWdlIFNpbGhvdWV0dGUgLS0+CiAgPHJlY3QgeD0iMCIgeT0iMzgwIiB3aWR0aD0iODAwIiBoZWlnaHQ9IjEyMCIgZmlsbD0iIzAzMDIwNyIgLz4KICA8IS0tIEJhbmQgU2lsaG91ZXR0ZXMgb24gU3RhZ2UgLS0+CiAgPGNpcmNsZSBjeD0iMTgwIiBjeT0iMzQwIiByPSIxNCIgZmlsbD0iIzAwMCIgLz48cGF0aCBkPSJNIDE2NSwzODAgTCAxOTUsMzgwIEwgMTg4LDM1NCBMIDE3MiwzNTQgWiIgZmlsbD0iIzAwMCIgLz4KICA8Y2lyY2xlIGN4PSIyNTAiIGN5PSIzMzUiIHI9IjE0IiBmaWxsPSIjMDAwIiAvPjxwYXRoIGQ9Ik0gMjM1LDM4MCBMIDI2NSwzODAgTCAyNTgsMzQ5IEwgMjQyLDM0OSBaIiBmaWxsPSIjMDAwIiAvPgogIDxjaXJjbGUgY3g9IjMyMCIgY3k9IjMzMCIgcj0iMTUiIGZpbGw9IiMwMDAiIC8+PHBhdGggZD0iTSAzMDUsMzgwIEwgMzM1LDM4MCBMIDMyOCwzNDQgTCAzMTIsMzQ0IFoiIGZpbGw9IiMwMDAiIC8+CiAgPGNpcmNsZSBjeD0iNDAwIiBjeT0iMzI1IiByPSIxNiIgZmlsbD0iIzAwMCIgLz48cGF0aCBkPSJNIDM4MywzODAgTCA0MTcsMzgwIEwgNDEwLDM0MCBMIDM5MCwzNDAgWiIgZmlsbD0iIzAwMCIgLz4KICA8Y2lyY2xlIGN4PSI0ODAiIGN5PSIzMzAiIHI9IjE1IiBmaWxsPSIjMDAwIiAvPjxwYXRoIGQ9Ik0gNDY1LDM4MCBMIDQ5NSwzODAgTCA0ODgsMzQ0IEwgNDcyLDM0NCBaIiBmaWxsPSIjMDAwIiAvPgogIDxjaXJjbGUgY3g9IjU1MCIgY3k9IjMzNSIgcj0iMTQiIGZpbGw9IiMwMDAiIC8+PHBhdGggZD0iTSA1MzUsMzgwIEwgNTY1LDM4MCBMIDU1OCwzNDkgTCA1NDIsMzQ5IFoiIGZpbGw9IiMwMDAiIC8+CiAgPGNpcmNsZSBjeD0iNjIwIiBjeT0iMzQwIiByPSIxNCIgZmlsbD0iIzAwMCIgLz48cGF0aCBkPSJNIDYwNSwzODAgTCA2MzUsMzgwIEwgNjI4LDM1NCBMIDYxMiwzNTQgWiIgZmlsbD0iIzAwMCIgLz4KICA8IS0tIEdsb3dpbmcgTGlnaHRzdGlja3MgaW4gQ3Jvd2QgLS0+CiAgPGNpcmNsZSBjeD0iMTIwIiBjeT0iNDQwIiByPSI0IiBmaWxsPSIjZTBlN2ZmIiAvPgogIDxjaXJjbGUgY3g9IjIyMCIgY3k9IjQ2MCIgcj0iNSIgZmlsbD0iI2MwODRmYyIgLz4KICA8Y2lyY2xlIGN4PSIzNDAiIGN5PSI0MzAiIHI9IjQiIGZpbGw9IiNmNDcyYjYiIC8+CiAgPGNpcmNsZSBjeD0iNDUwIiBjeT0iNDUwIiByPSI1IiBmaWxsPSIjNjBhNWZhIiAvPgogIDxjaXJjbGUgY3g9IjU4MCIgY3k9IjQzNSIgcj0iNCIgZmlsbD0iI2MwODRmYyIgLz4KICA8Y2lyY2xlIGN4PSI2ODAiIGN5PSI0NjAiIHI9IjUiIGZpbGw9IiNlMGU3ZmYiIC8+CiAgPCEtLSBCYW5uZXIgVGV4dCAtLT4KICA8dGV4dCB4PSI0MDAiIHk9IjE2MCIgZm9udC1mYW1pbHk9Ii1hcHBsZS1zeXN0ZW0sIHNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iNDQiIGZpbGw9IiNmZmZmZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSI0Ij5TVFJBWSBLSURTIFdPUkxEIFRPVVI8L3RleHQ+CiAgPHRleHQgeD0iNDAwIiB5PSIyMTAiIGZvbnQtZmFtaWx5PSItYXBwbGUtc3lzdGVtLCBzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iNzAwIiBmb250LXNpemU9IjI0IiBmaWxsPSIjZWM0ODk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iNiI+RE9NSU5BVEUgMjAyNiDigKIgT0ZGSUNJQUwgREFURVM8L3RleHQ+Cjwvc3ZnPg==",
        studio: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNTAwIiB3aWR0aD0iODAwIiBoZWlnaHQ9IjUwMCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI1MDAiIGZpbGw9IiMwZjE3MmEiIC8+CiAgPCEtLSBTdHVkaW8gTW9uaXRvciBTY3JlZW5zIC0tPgogIDxyZWN0IHg9IjE1MCIgeT0iNjAiIHdpZHRoPSI1MDAiIGhlaWdodD0iMjQwIiByeD0iMTIiIGZpbGw9IiMxZTI5M2IiIHN0cm9rZT0iIzMzNDE1NSIgc3Ryb2tlLXdpZHRoPSI0IiAvPgogIDwhLS0gV2F2ZWZvcm0gVHJhY2tzIC0tPgogIDxwYXRoIGQ9Ik0gMTcwLDEyMCBRIDIyMCw3MCAyNzAsMTIwIFQgMzcwLDEyMCBUIDQ3MCwxMjAgVCA1NzAsMTIwIFQgNjMwLDEyMCIgc3Ryb2tlPSIjMzhiZGY4IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIC8+CiAgPHBhdGggZD0iTSAxNzAsMTcwIFEgMjEwLDIxMCAyNTAsMTcwIFQgMzUwLDE3MCBUIDQ1MCwxNzAgVCA1NTAsMTcwIFQgNjMwLDE3MCIgc3Ryb2tlPSIjYTg1NWY3IiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIC8+CiAgPHBhdGggZD0iTSAxNzAsMjIwIFEgMjMwLDE4MCAyOTAsMjIwIFQgMzkwLDIyMCBUIDQ5MCwyMjAgVCA1OTAsMjIwIFQgNjMwLDIyMCIgc3Ryb2tlPSIjZjQzZjVlIiBzdHJva2Utd2lkdGg9IjMiIGZpbGw9Im5vbmUiIC8+CiAgPCEtLSBNaXhpbmcgQ29uc29sZSBEZXNrIC0tPgogIDxyZWN0IHg9IjgwIiB5PSIzMjAiIHdpZHRoPSI2NDAiIGhlaWdodD0iMTUwIiByeD0iMTYiIGZpbGw9IiMwMjA2MTciIHN0cm9rZT0iIzFlMjkzYiIgc3Ryb2tlLXdpZHRoPSI0IiAvPgogIDwhLS0gU2xpZGVycyAmIEtub2JzIC0tPgogIDxyZWN0IHg9IjE0MCIgeT0iMzUwIiB3aWR0aD0iOCIgaGVpZ2h0PSI4MCIgcng9IjQiIGZpbGw9IiMzMzQxNTUiIC8+CiAgPHJlY3QgeD0iMTM0IiB5PSIzODAiIHdpZHRoPSIyMCIgaGVpZ2h0PSIxMiIgcng9IjMiIGZpbGw9IiMzOGJkZjgiIC8+CiAgPHJlY3QgeD0iMjIwIiB5PSIzNTAiIHdpZHRoPSI4IiBoZWlnaHQ9IjgwIiByeD0iNCIgZmlsbD0iIzMzNDE1NSIgLz4KICA8cmVjdCB4PSIyMTQiIHk9IjM2NSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjEyIiByeD0iMyIgZmlsbD0iI2E4NTVmNyIgLz4KICA8cmVjdCB4PSIzMDAiIHk9IjM1MCIgd2lkdGg9IjgiIGhlaWdodD0iODAiIHJ4PSI0IiBmaWxsPSIjMzM0MTU1IiAvPgogIDxyZWN0IHg9IjI5NCIgeT0iNDAwIiB3aWR0aD0iMjAiIGhlaWdodD0iMTIiIHJ4PSIzIiBmaWxsPSIjZjQzZjVlIiAvPgogIDxjaXJjbGUgY3g9IjQ1MCIgY3k9IjM4MCIgcj0iMTYiIGZpbGw9IiMxZTI5M2IiIHN0cm9rZT0iIzM4YmRmOCIgc3Ryb2tlLXdpZHRoPSIzIiAvPgogIDxjaXJjbGUgY3g9IjUyMCIgY3k9IjM4MCIgcj0iMTYiIGZpbGw9IiMxZTI5M2IiIHN0cm9rZT0iI2E4NTVmNyIgc3Ryb2tlLXdpZHRoPSIzIiAvPgogIDxjaXJjbGUgY3g9IjU5MCIgY3k9IjM4MCIgcj0iMTYiIGZpbGw9IiMxZTI5M2IiIHN0cm9rZT0iI2Y0M2Y1ZSIgc3Ryb2tlLXdpZHRoPSIzIiAvPgogIDx0ZXh0IHg9IjQwMCIgeT0iNDgwIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9IjgwMCIgZm9udC1zaXplPSIyMCIgZmlsbD0iIzk0YTNiOCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+M1JBQ0hBIFJFQ09SRElORyBTVFVESU8g4oCiIFJFQ09SRElORyBJTiBQUk9HUkVTUzwvdGV4dD4KPC9zdmc+",
        brownies: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNTAwIiB3aWR0aD0iODAwIiBoZWlnaHQ9IjUwMCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI1MDAiIGZpbGw9IiMyOTE4MTAiIC8+CiAgPCEtLSBUcmF5IC0tPgogIDxyZWN0IHg9IjEwMCIgeT0iODAiIHdpZHRoPSI2MDAiIGhlaWdodD0iMzQwIiByeD0iMjAiIGZpbGw9IiM0MjJhMWQiIHN0cm9rZT0iIzVjM2EyOCIgc3Ryb2tlLXdpZHRoPSI2IiAvPgogIDwhLS0gQnJvd25pZSBTcXVhcmVzIC0tPgogIDxyZWN0IHg9IjE1MCIgeT0iMTIwIiB3aWR0aD0iMTQwIiBoZWlnaHQ9IjEyMCIgcng9IjEwIiBmaWxsPSIjMWMwZDA2IiAvPgogIDxyZWN0IHg9IjMzMCIgeT0iMTIwIiB3aWR0aD0iMTQwIiBoZWlnaHQ9IjEyMCIgcng9IjEwIiBmaWxsPSIjMWMwZDA2IiAvPgogIDxyZWN0IHg9IjUxMCIgeT0iMTIwIiB3aWR0aD0iMTQwIiBoZWlnaHQ9IjEyMCIgcng9IjEwIiBmaWxsPSIjMWMwZDA2IiAvPgogIDxyZWN0IHg9IjE1MCIgeT0iMjcwIiB3aWR0aD0iMTQwIiBoZWlnaHQ9IjEyMCIgcng9IjEwIiBmaWxsPSIjMWMwZDA2IiAvPgogIDxyZWN0IHg9IjMzMCIgeT0iMjcwIiB3aWR0aD0iMTQwIiBoZWlnaHQ9IjEyMCIgcng9IjEwIiBmaWxsPSIjMWMwZDA2IiAvPgogIDxyZWN0IHg9IjUxMCIgeT0iMjcwIiB3aWR0aD0iMTQwIiBoZWlnaHQ9IjEyMCIgcng9IjEwIiBmaWxsPSIjMWMwZDA2IiAvPgogIDwhLS0gQ2hvY29sYXRlIENoaXBzICYgRHJpenpsZSAtLT4KICA8Y2lyY2xlIGN4PSIyMDAiIGN5PSIxNjAiIHI9IjYiIGZpbGw9IiM1MjMxMjEiIC8+PGNpcmNsZSBjeD0iMjMwIiBjeT0iMTgwIiByPSI4IiBmaWxsPSIjNTIzMTIxIiAvPgogIDxjaXJjbGUgY3g9IjM4MCIgY3k9IjE2MCIgcj0iNyIgZmlsbD0iIzUyMzEyMSIgLz48Y2lyY2xlIGN4PSI0MTAiIGN5PSIxOTAiIHI9IjYiIGZpbGw9IiM1MjMxMjEiIC8+CiAgPGNpcmNsZSBjeD0iNTYwIiBjeT0iMTUwIiByPSI4IiBmaWxsPSIjNTIzMTIxIiAvPjxjaXJjbGUgY3g9IjU5MCIgY3k9IjE4MCIgcj0iNiIgZmlsbD0iIzUyMzEyMSIgLz4KICA8dGV4dCB4PSI0MDAiIHk9IjQ2NSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMjQiIGZpbGw9IiNmYmJmMjQiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkZFTElYJ1MgU1BFQ0lBTCBIT01FTUFERSBCUk9XTklFUyDwn42q4pyoPC90ZXh0Pgo8L3N2Zz4=",
        cat: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNTAwIiB3aWR0aD0iODAwIiBoZWlnaHQ9IjUwMCI+CiAgPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI1MDAiIGZpbGw9IiMwZjE3MmEiIC8+CiAgPCEtLSBDYXQgSGVhZCAtLT4KICA8Y2lyY2xlIGN4PSI0MDAiIGN5PSIyNjAiIHI9IjEyMCIgZmlsbD0iI2Q5NzcwNiIgLz4KICA8IS0tIEVhcnMgLS0+CiAgPHBvbHlnb24gcG9pbnRzPSIzMDAsMTgwIDI2MCw3MCAzNTAsMTUwIiBmaWxsPSIjZDk3NzA2IiAvPgogIDxwb2x5Z29uIHBvaW50cz0iMzAwLDE4MCAyNzUsOTAgMzQwLDE1NSIgZmlsbD0iI2ZlZjA4YSIgLz4KICA8cG9seWdvbiBwb2ludHM9IjUwMCwxODAgNTQwLDcwIDQ1MCwxNTAiIGZpbGw9IiNkOTc3MDYiIC8+CiAgPHBvbHlnb24gcG9pbnRzPSI1MDAsMTgwIDUyNSw5MCA0NjAsMTU1IiBmaWxsPSIjZmVmMDhhIiAvPgogIDwhLS0gRXllcyAtLT4KICA8ZWxsaXBzZSBjeD0iMzUwIiBjeT0iMjQwIiByeD0iMjAiIHJ5PSIyOCIgZmlsbD0iIzIyYzU1ZSIgLz4KICA8ZWxsaXBzZSBjeD0iNDUwIiBjeT0iMjQwIiByeD0iMjAiIHJ5PSIyOCIgZmlsbD0iIzIyYzU1ZSIgLz4KICA8ZWxsaXBzZSBjeD0iMzUwIiBjeT0iMjQwIiByeD0iNiIgcnk9IjIyIiBmaWxsPSIjMDUyZTE2IiAvPgogIDxlbGxpcHNlIGN4PSI0NTAiIGN5PSIyNDAiIHJ4PSI2IiByeT0iMjIiIGZpbGw9IiMwNTJlMTYiIC8+CiAgPCEtLSBOb3NlICYgV2hpc2tlcnMgLS0+CiAgPHBvbHlnb24gcG9pbnRzPSI0MDAsMjcwIDM5MCwyODUgNDEwLDI4NSIgZmlsbD0iI2Y0M2Y1ZSIgLz4KICA8bGluZSB4MT0iMzEwIiB5MT0iMjgwIiB4Mj0iMjEwIiB5Mj0iMjcwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iNCIgLz4KICA8bGluZSB4MT0iMzEwIiB5MT0iMjk1IiB4Mj0iMjAwIiB5Mj0iMzAwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iNCIgLz4KICA8bGluZSB4MT0iNDkwIiB5MT0iMjgwIiB4Mj0iNTkwIiB5Mj0iMjcwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iNCIgLz4KICA8bGluZSB4MT0iNDkwIiB5MT0iMjk1IiB4Mj0iNjAwIiB5Mj0iMzAwIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iNCIgLz4KICA8dGV4dCB4PSI0MDAiIHk9IjQ0MCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc2l6ZT0iMjYiIGZpbGw9IiNmZWYwOGEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlNPT05JIFNBWVMgSEkgVE8gU1RBWXMhIPCfkLHinaTvuI88L3RleHQ+Cjwvc3ZnPg=="
    };
    let userAvatarUrl = AVATARS.gaerwenill;
    let attachedImgData = null;
    const MEMBERS = [
        { key: "bangchan", name: "Bang Chan", handle: "@gnabnahc", avatar: AVATARS.bangchan, responses: ["Thank you @gaerwenill! We will work super hard for STAYs! ❤️", "Late night in 3RACHA studio... can you bring iced americanos? ☕", "Chanie's Room live stream tonight! Will tell STAYs about your schedule!", "You're the best manager @gaerwenill! 👍✨"] },
        { key: "leeknow", name: "Lee Know", handle: "@t.leeknowsaurus", avatar: AVATARS.leeknow, responses: ["Did Sooni, Doongi, and Dori approve this post @gaerwenill? 🐱", "Manager @gaerwenill, where is my pudding?", "Dancing 8 hours today. Legs are fine, patience is not 😏", "Nice post! Now buy us meat 🥩"] },
        { key: "changbin", name: "Changbin", handle: "@jutdwae", avatar: AVATARS.changbin, responses: ["JUTDAE! We do things with conviction! 💪🔥", "Did you see my bicep gains in today's photoshoot @gaerwenill?!", "3RACHA in the building! 🎵", "Protein shake finished, back to lyrics!"] },
        { key: "hyunjin", name: "Hyunjin", handle: "@hynjinnnn", avatar: AVATARS.hyunjin, responses: ["The aesthetic of this concert stage is stunning @gaerwenill! 🎨✨", "Kami bit my sock again 😭 help me manager!", "Dramatic? Me?! I'm simply expressing my soul! 🎭"] },
        { key: "han", name: "Han Jisung", handle: "@_doolsetnet", avatar: AVATARS.han, responses: ["I wrote 3 songs in my sleep last night! You're welcome @gaerwenill 🎵", "Can we order cheesecake for lunch? Lyrical inspiration!", "STAY!! I missed you guys so much!"] },
        { key: "felix", name: "Felix", handle: "@yong.lixx", avatar: AVATARS.felix, responses: ["Baked homemade brownies for @gaerwenill & the boys! 🍪", "Hope everyone stays warm today! ☀️❤️", "Deep voice practice done! Ready to shake the stage! 🔊", "Manager @gaerwenill is the best! Thank you!"] },
        { key: "seungmin", name: "Seungmin", handle: "@miniverse.___", avatar: AVATARS.seungmin, responses: ["Vocal practice finished! Ready for comeback @gaerwenill 🐶", "Changbin hyung is being noisy during my nap...", "Day 1290 of teasing Changbin hyung. Going great."] },
        { key: "in", name: "I.N", handle: "@i.2.n.8", avatar: AVATARS.in, responses: ["Look at my OOTD for today's schedule @gaerwenill! 😎👔", "The hyungs bought me dinner again. Maknae wins! 🥖", "Maknae energy fully loaded! ⚡"] }
    ];
    const STORIES = [
        { id: 1, author: "Bang Chan", handle: "@gnabnahc", avatar: AVATARS.bangchan, img: PHOTOS.studio, caption: "Late night producing in 3RACHA studio... 🎧", time: "12m ago" },
        { id: 2, author: "Felix", handle: "@yong.lixx", avatar: AVATARS.felix, img: PHOTOS.brownies, caption: "Freshly baked brownies for @gaerwenill & the team! 🍪", time: "30m ago" },
        { id: 3, author: "Lee Know", handle: "@t.leeknowsaurus", avatar: AVATARS.leeknow, img: PHOTOS.cat, caption: "Sooni says hi to STAYs! 🐱", time: "1h ago" },
        { id: 4, author: "Hyunjin", handle: "@hynjinnnn", avatar: AVATARS.hyunjin, img: PHOTOS.studio, caption: "New track arrangement finished! 🎨", time: "2h ago" },
        { id: 5, author: "Changbin", handle: "@jutdwae", avatar: AVATARS.changbin, img: PHOTOS.concert, caption: "Morning workout done! Conviction! 💪", time: "3h ago" }
    ];
    let posts = [
        {
            id: 101,
            author: "Bang Chan",
            handle: "@gnabnahc",
            avatar: AVATARS.bangchan,
            time: "15m ago",
            content: "Official Announcement: Stray Kids World Tour 2026 dates are officially locked in! Huge thanks to our Head Manager @gaerwenill for organizing this schedule! STAY get ready! 🧭✨ #StrayKids #JYPE",
            img: PHOTOS.concert,
            likes: 42800,
            liked: false,
            comments: [
                { id: 1, author: "Felix", handle: "@yong.lixx", avatar: AVATARS.felix, text: "Let's go hyung!! Made celebratory brownies for @gaerwenill! ❤️🍪" },
                { id: 2, author: "Sarah (STAY)", handle: "@felix_sunshine_stay", avatar: AVATARS.stay1, text: "THANK YOU MANAGER @gaerwenill FOR PROTECTING OUR BOYS!! 😭😭💖" },
                { id: 3, author: "Lee Know", handle: "@t.leeknowsaurus", avatar: AVATARS.leeknow, text: "Does the tour schedule include pudding breaks @gaerwenill?" }
            ]
        },
        {
            id: 102,
            author: "Dispatch Official",
            handle: "@kpop_dispatch",
            avatar: AVATARS.dispatch,
            time: "45m ago",
            content: "🚨 BREAKING: Stray Kids spotted arriving at JYP Studios with Head Manager @gaerwenill. Insiders report new album recording is 90% complete!",
            img: PHOTOS.studio,
            likes: 89100,
            liked: false,
            comments: [
                { id: 1, author: "STAY World News", handle: "@stay_updates", avatar: AVATARS.stay2, text: "STAYs WE ARE GETTING A COMEBACK!! Thank you @gaerwenill!! 🔥" },
                { id: 2, author: "Changbin", handle: "@jutdwae", avatar: AVATARS.changbin, text: "3RACHA tracks are going to blow STAYs minds! 💪" }
            ]
        }
    ];
    let activeDMIndex = 0;
    let dmMessages = {
        0: [
            { sender: "them", text: "Hey @gaerwenill! Are the world tour stage designs ready?" },
            { sender: "me", text: "Yes Chan! Just finalized with JYPE production team!" },
            { sender: "them", text: "Awesome! STAYs are going to love Chanie's Room tonight! 👍" }
        ],
        1: [
            { sender: "them", text: "Manager @gaerwenill, where is my pudding?" },
            { sender: "me", text: "In the fridge behind Sooni's treats!" }
        ]
    };
    window.onload = function() {
        renderStories();
        renderFeed();
        renderDMSidebar();
        renderDMChat();
    };
    function switchTab(tabName) {
        document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
        document.getElementById('tab-' + tabName).classList.add('active');
        document.getElementById('nav-' + tabName).classList.add('active');
        if(tabName === 'profile') renderProfileUserPosts();
    }
    function renderStories() {
        const bar = document.getElementById('storiesBar');
        let html = '';
        STORIES.forEach((s, idx) => {
            html += `<div class="story-item" onclick="openStory(${idx})"><div class="story-ring"><img class="story-avatar" src="${s.avatar}" alt="${s.author}"></div><div class="story-username">${s.author}</div></div>`;
        });
        bar.innerHTML = html;
    }
    let activeStoryIdx = 0;
    function openStory(idx) {
        activeStoryIdx = idx;
        const s = STORIES[idx];
        document.getElementById('storyModalAvatar').src = s.avatar;
        document.getElementById('storyModalTitle').innerText = s.author;
        document.getElementById('storyModalTime').innerText = s.time;
        document.getElementById('storyModalImg').src = s.img;
        document.getElementById('storyModalCaption').innerText = s.caption;
        const modal = document.getElementById('storyModal');
        modal.classList.add('active');
        const bar = document.getElementById('storyProgress');
        bar.style.animation = 'none'; bar.offsetHeight; bar.style.animation = 'storyTimer 5s linear forwards';
    }
    function closeStory() { document.getElementById('storyModal').classList.remove('active'); }
    function sendStoryReply() {
        const input = document.getElementById('storyReplyInput');
        if(input.value.trim() !== '') { alert('Reply sent to ' + STORIES[activeStoryIdx].author + ': "' + input.value + '"'); input.value = ''; closeStory(); }
    }
    function renderFeed() {
        const container = document.getElementById('feedPosts');
        let html = '';
        posts.forEach(post => {
            let imgHTML = post.img ? `<img class="post-image-card" src="${post.img}" alt="Post image">` : '';
            let commentsHTML = '';
            post.comments.forEach(c => {
                commentsHTML += `<div class="comment-item"><img class="comment-avatar" src="${c.avatar}" alt="${c.author}"><div class="comment-body"><div class="comment-author-row"><span class="comment-author">${c.author}</span><span class="comment-handle">${c.handle}</span></div><div class="comment-text">${c.text}</div><button class="comment-reply-btn" onclick="toggleInlineReply(${post.id}, ${c.id})">💬 Reply</button><div class="inline-reply-box" id="replyBox_${post.id}_${c.id}"><input type="text" class="inline-reply-input" id="replyInput_${post.id}_${c.id}" placeholder="Reply to ${c.author}..."><button class="inline-reply-send" onclick="submitCommentReply(${post.id}, '${c.author}')">Send</button></div></div></div>`;
            });
            html += `<div class="post"><img class="post-avatar" src="${post.avatar}" alt="${post.author}"><div class="post-content"><div class="post-header"><span class="post-author">${post.author}</span><span class="verified-badge">✔</span><span class="post-handle">${post.handle} • ${post.time}</span></div><div class="post-text">${post.content}</div>${imgHTML}<div class="post-actions"><div class="action-item ${post.liked ? 'liked' : ''}" onclick="toggleLike(${post.id})"><span>${post.liked ? '❤️' : '🤍'}</span><span>${post.likes.toLocaleString()}</span></div><div class="action-item"><span>💬</span><span>${post.comments.length}</span></div><div class="action-item"><span>🔁</span><span>Share</span></div></div><div class="comments-list">${commentsHTML}</div></div></div>`;
        });
        container.innerHTML = html;
    }
    function toggleLike(postId) {
        const post = posts.find(p => p.id === postId);
        if(post) { post.liked = !post.liked; post.likes += post.liked ? 1 : -1; renderFeed(); }
    }
    function toggleInlineReply(postId, commentId) {
        const box = document.getElementById(`replyBox_${postId}_${commentId}`);
        if(box) box.classList.toggle('active');
    }
    function submitCommentReply(postId, replyToAuthor) {
        const post = posts.find(p => p.id === postId);
        if(post) {
            post.comments.push({ id: Date.now(), author: "Gaerwenill", handle: "@gaerwenill", avatar: userAvatarUrl, text: `Replying to @${replyToAuthor}: Thank you for supporting Stray Kids!` });
            renderFeed();
            setTimeout(() => {
                const randomMem = MEMBERS[Math.floor(Math.random() * MEMBERS.length)];
                post.comments.push({ id: Date.now() + 1, author: randomMem.name, handle: randomMem.handle, avatar: randomMem.avatar, text: randomMem.responses[Math.floor(Math.random() * randomMem.responses.length)] });
                renderFeed();
            }, 1500);
        }
    }
    function handleImgAttach(event) {
        const file = event.target.files[0];
        if(file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                attachedImgData = e.target.result;
                document.getElementById('previewImgTag').src = attachedImgData;
                document.getElementById('imagePreviewBox').style.display = 'block';
            }
            reader.readAsDataURL(file);
        }
    }
    function removeAttachedImg() {
        attachedImgData = null;
        document.getElementById('imagePreviewBox').style.display = 'none';
        document.getElementById('postImgInput').value = '';
    }
    function publishNewPost() {
        const text = document.getElementById('newPostText').value.trim();
        if(!text && !attachedImgData) { alert("Please write a post or attach an image!"); return; }
        const newPost = { id: Date.now(), author: "Gaerwenill", handle: "@gaerwenill", avatar: userAvatarUrl, time: "Just now", content: text, img: attachedImgData, likes: Math.floor(Math.random() * 5000) + 1200, liked: false, comments: [] };
        posts.unshift(newPost);
        document.getElementById('newPostText').value = '';
        removeAttachedImg();
        renderFeed();
        setTimeout(() => {
            const bot1 = MEMBERS[0]; const bot2 = MEMBERS[5];
            const bot3 = { name: "Sarah (STAY)", handle: "@felix_sunshine_stay", avatar: AVATARS.stay1, text: "WE LOVE YOU MANAGER @gaerwenill!! THANK YOU FOR EVERYTHING! 💖" };
            newPost.comments.push({ id: 1, author: bot1.name, handle: bot1.handle, avatar: bot1.avatar, text: bot1.responses[0] });
            newPost.comments.push({ id: 2, author: bot2.name, handle: bot2.handle, avatar: bot2.avatar, text: bot2.responses[0] });
            newPost.comments.push({ id: 3, author: bot3.name, handle: bot3.handle, avatar: bot3.avatar, text: bot3.text });
            renderFeed();
        }, 2000);
    }
    function handleProfilePicChange(event) {
        const file = event.target.files[0];
        if(file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                userAvatarUrl = e.target.result;
                document.getElementById('topHeaderAvatar').src = userAvatarUrl;
                document.getElementById('createPostUserAvatar').src = userAvatarUrl;
                document.getElementById('profileAvatarImg').src = userAvatarUrl;
                alert("Profile photo updated successfully!");
            }
            reader.readAsDataURL(file);
        }
    }
    function renderDMSidebar() {
        const sidebar = document.getElementById('dmSidebar');
        let html = '';
        MEMBERS.forEach((m, idx) => {
            html += `<div class="dm-member-item ${idx === activeDMIndex ? 'active' : ''}" onclick="selectDMMember(${idx})"><img class="dm-member-avatar" src="${m.avatar}" alt="${m.name}"><div class="dm-member-name">${m.name}</div></div>`;
        });
        sidebar.innerHTML = html;
    }
    function selectDMMember(idx) { activeDMIndex = idx; renderDMSidebar(); renderDMChat(); }
    function renderDMChat() {
        const member = MEMBERS[activeDMIndex];
        document.getElementById('dmActiveAvatar').src = member.avatar;
        document.getElementById('dmActiveTitle').innerText = member.name;
        const chatContainer = document.getElementById('dmChatMessages');
        let msgs = dmMessages[activeDMIndex] || [{ sender: "them", text: `Hey Manager @gaerwenill! Ready for today's schedule!` }];
        let html = '';
        msgs.forEach(m => { html += `<div class="chat-bubble ${m.sender === 'me' ? 'outgoing' : 'incoming'}">${m.text}</div>`; });
        chatContainer.innerHTML = html;
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    function sendDM() {
        const input = document.getElementById('dmInputText');
        const text = input.value.trim();
        if(text) {
            if(!dmMessages[activeDMIndex]) dmMessages[activeDMIndex] = [];
            dmMessages[activeDMIndex].push({ sender: "me", text: text });
            input.value = '';
            renderDMChat();
            setTimeout(() => {
                const member = MEMBERS[activeDMIndex];
                const reply = member.responses[Math.floor(Math.random() * member.responses.length)];
                dmMessages[activeDMIndex].push({ sender: "them", text: reply });
                renderDMChat();
            }, 1500);
        }
    }
    function renderProfileUserPosts() {
        const container = document.getElementById('profileUserPosts');
        const userPosts = posts.filter(p => p.author === "Gaerwenill");
        let html = '';
        if(userPosts.length === 0) {
            html = '<div style="padding: 20px; color: #64748b; text-align: center;">No posts yet. Write your first update in the Feed tab!</div>';
        } else {
            userPosts.forEach(post => {
                let imgHTML = post.img ? `<img class="post-image-card" src="${post.img}" alt="Post image">` : '';
                html += `<div class="post"><img class="post-avatar" src="${post.avatar}" alt="${post.author}"><div class="post-content"><div class="post-header"><span class="post-author">${post.author}</span><span class="verified-badge">✔</span><span class="post-handle">${post.handle} • ${post.time}</span></div><div class="post-text">${post.content}</div>${imgHTML}</div></div>`;
            });
        }
        container.innerHTML = html;
    }
</script>
</body>
</html>"""

components.html(html_content, height=850, scrolling=True)
