import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - Stray Kids",
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
    .block-container { padding: 0rem !important; margin: 0rem !important; max-width: 100% !important; }
    iframe { width: 100% !important; height: 100vh !important; border: none !important; }
</style>
""",
    unsafe_allow_html=True,
)

# Inline SVG Data URIs for crisp avatars and images
AVATAR_CHAN = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%232a1b4e'/><circle cx='50' cy='38' r='20' fill='%23a855f7'/><circle cx='50' cy='90' r='35' fill='%23a855f7'/><text x='50' y='43' font-size='16' font-weight='bold' fill='white' text-anchor='middle'>BC</text></svg>"
AVATAR_FELIX = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%234c0519'/><circle cx='50' cy='38' r='20' fill='%23f43f5e'/><circle cx='50' cy='90' r='35' fill='%23f43f5e'/><text x='50' y='43' font-size='16' font-weight='bold' fill='white' text-anchor='middle'>FL</text></svg>"
AVATAR_LEEKNOW = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23064e3b'/><circle cx='50' cy='38' r='20' fill='%2310b981'/><circle cx='50' cy='90' r='35' fill='%2310b981'/><text x='50' y='43' font-size='16' font-weight='bold' fill='white' text-anchor='middle'>LK</text></svg>"
AVATAR_HYUNJIN = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%231e1b4b'/><circle cx='50' cy='38' r='20' fill='%236366f1'/><circle cx='50' cy='90' r='35' fill='%236366f1'/><text x='50' y='43' font-size='16' font-weight='bold' fill='white' text-anchor='middle'>HJ</text></svg>"
AVATAR_HAN = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%2378350f'/><circle cx='50' cy='38' r='20' fill='%23f59e0b'/><circle cx='50' cy='90' r='35' fill='%23f59e0b'/><text x='50' y='43' font-size='16' font-weight='bold' fill='white' text-anchor='middle'>HN</text></svg>"
AVATAR_DISPATCH = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%231e293b'/><circle cx='50' cy='38' r='20' fill='%233b82f6'/><circle cx='50' cy='90' r='35' fill='%233b82f6'/><text x='50' y='43' font-size='16' font-weight='bold' fill='white' text-anchor='middle'>DP</text></svg>"
AVATAR_STAY = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23831843'/><circle cx='50' cy='38' r='20' fill='%23ec4899'/><circle cx='50' cy='90' r='35' fill='%23ec4899'/><text x='50' y='43' font-size='16' font-weight='bold' fill='white' text-anchor='middle'>STAY</text></svg>"
AVATAR_MANAGER = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23581c87'/><circle cx='50' cy='38' r='20' fill='%23c084fc'/><circle cx='50' cy='90' r='35' fill='%23c084fc'/><text x='50' y='43' font-size='16' font-weight='bold' fill='white' text-anchor='middle'>MGR</text></svg>"

MEDIA_STUDIO = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 350'><rect width='600' height='350' fill='%230f172a'/><text x='300' y='160' font-size='28' font-weight='bold' fill='%23a855f7' text-anchor='middle'>🎵 3RACHA RECORDING STUDIO</text><text x='300' y='200' font-size='16' fill='%2394a3b8' text-anchor='middle'>Track 03 Recording Session Completed</text></svg>"
MEDIA_COOKIES = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 350'><rect width='600' height='350' fill='%23271a0c'/><text x='300' y='160' font-size='28' font-weight='bold' fill='%23f59e0b' text-anchor='middle'>🍪 FELIX HOMEMADE BROWNIES</text><text x='300' y='200' font-size='16' fill='%23d97706' text-anchor='middle'>Baked with love for @gaerwenill & SKZ</text></svg>"
MEDIA_DISPATCH = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 350'><rect width='600' height='350' fill='%23020617'/><text x='300' y='150' font-size='32' font-weight='bold' fill='%23ef4444' text-anchor='middle'>🚨 DISPATCH EXCLUSIVE</text><text x='300' y='200' font-size='18' fill='%23f87171' text-anchor='middle'>Manager @gaerwenill spotted at JYP Center</text></svg>"

html_code = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Status AI - SKZ</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; -webkit-tap-highlight-color: transparent; }}
        body {{ background-color: #000000; color: #e7e9ea; display: flex; justify-content: center; min-height: 100vh; overflow-x: hidden; }}
        
        .app-container {{
            width: 100%;
            max-width: 480px;
            background-color: #000000;
            min-height: 100vh;
            border-left: 1px solid #16181c;
            border-right: 1px solid #16181c;
            display: flex;
            flex-direction: column;
            position: relative;
            padding-bottom: 75px;
        }}

        /* HEADER */
        .top-header {{
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.92);
            backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
            z-index: 100; padding: 12px 16px;
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #16181c;
        }}
        .app-logo {{
            font-size: 21px; font-weight: 900; letter-spacing: -0.5px;
            background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 6px;
        }}
        .energy-badge {{
            background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3);
            padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;
        }}

        /* STORIES BAR */
        .stories-section {{ border-bottom: 1px solid #16181c; padding: 12px 0; background: #000; }}
        .stories-container {{
            display: flex; gap: 14px; padding: 0 16px; overflow-x: auto;
            scrollbar-width: none; -ms-overflow-style: none;
        }}
        .stories-container::-webkit-scrollbar {{ display: none; }}
        
        .story-item {{ display: flex; flex-direction: column; align-items: center; gap: 5px; cursor: pointer; flex-shrink: 0; }}
        .story-ring {{
            width: 66px; height: 66px; border-radius: 50%; padding: 2.5px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
            transition: transform 0.2s;
        }}
        .story-ring:active {{ transform: scale(0.95); }}
        .story-ring.my-story {{ background: #2f3336; }}
        .story-avatar {{ width: 59px; height: 59px; border-radius: 50%; border: 2.5px solid #000; object-fit: cover; background: #16181c; }}
        .story-username {{ font-size: 11px; color: #71767b; width: 68px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500; }}

        /* FEED POSTS */
        .feed {{ display: flex; flex-direction: column; }}
        .post {{ padding: 14px 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; }}
        .post-avatar {{ width: 46px; height: 46px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #16181c; }}
        .post-content {{ flex: 1; min-width: 0; }}
        .post-header {{ display: flex; align-items: center; gap: 4px; margin-bottom: 4px; flex-wrap: wrap; }}
        .post-author {{ font-weight: 700; font-size: 15px; color: #f7f9f9; }}
        .verified-badge {{ color: #1d9bf0; font-size: 14px; }}
        .post-handle {{ color: #71767b; font-size: 14px; }}
        .post-text {{ font-size: 15px; line-height: 1.45; color: #e7e9ea; margin-bottom: 10px; word-break: break-word; }}
        .post-image {{ width: 100%; max-height: 380px; object-fit: cover; border-radius: 16px; margin-bottom: 10px; border: 1px solid #2f3336; }}
        .post-actions {{ display: flex; justify-content: space-between; max-width: 340px; color: #71767b; font-size: 13px; margin-top: 6px; }}
        .action-btn {{ display: flex; align-items: center; gap: 6px; cursor: pointer; transition: color 0.2s; }}
        .action-btn:hover {{ color: #1d9bf0; }}
        .action-btn.liked {{ color: #f91880; }}

        /* CREATE POST */
        .create-post-box {{ padding: 14px 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #080a0f; }}
        .create-post-input {{ flex: 1; background: transparent; border: none; color: #fff; font-size: 15px; outline: none; resize: none; height: 50px; }}
        .publish-btn {{ background: linear-gradient(135deg, #a855f7, #ec4899); color: white; border: none; padding: 8px 18px; border-radius: 20px; font-weight: 700; font-size: 14px; cursor: pointer; align-self: flex-end; }}

        /* BOTTOM NAV */
        .bottom-nav {{
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.92); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 12px 0; z-index: 1000;
        }}
        .nav-item {{ color: #71767b; font-size: 20px; text-decoration: none; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 3px; }}
        .nav-item.active {{ color: #a855f7; }}
        .nav-label {{ font-size: 10px; font-weight: 600; }}

        .tab-content {{ display: none; }}
        .tab-content.active {{ display: block; }}

        /* DMS */
        .dm-header {{ padding: 14px 16px; font-weight: 800; border-bottom: 1px solid #16181c; font-size: 18px; display: flex; align-items: center; justify-content: space-between; }}
        .dm-member-select {{ display: flex; gap: 10px; padding: 12px 16px; overflow-x: auto; border-bottom: 1px solid #16181c; scrollbar-width: none; }}
        .dm-member-card {{ display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; opacity: 0.5; transition: opacity 0.2s; flex-shrink: 0; }}
        .dm-member-card.active {{ opacity: 1; }}
        .dm-member-avatar {{ width: 48px; height: 48px; border-radius: 50%; object-fit: cover; border: 2px solid #a855f7; }}
        .dm-member-name {{ font-size: 11px; font-weight: 600; color: #fff; }}

        .chat-container {{ padding: 16px; display: flex; flex-direction: column; gap: 12px; height: calc(100vh - 250px); overflow-y: auto; }}
        .chat-bubble {{ max-width: 82%; padding: 12px 16px; border-radius: 18px; font-size: 14px; line-height: 1.45; word-break: break-word; }}
        .chat-bubble.incoming {{ background: #161e27; color: #e7e9ea; align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid #2f3336; }}
        .chat-bubble.outgoing {{ background: linear-gradient(135deg, #8b5cf6, #ec4899); color: white; align-self: flex-end; border-bottom-right-radius: 4px; }}
        .chat-sender {{ font-size: 11px; font-weight: 700; margin-bottom: 4px; opacity: 0.8; }}
        
        .chat-input-bar {{ position: fixed; bottom: 62px; width: 100%; max-width: 480px; background: #000; padding: 10px 16px; display: flex; gap: 10px; border-top: 1px solid #16181c; }}
        .chat-input {{ flex: 1; background: #16181c; border: 1px solid #2f3336; border-radius: 20px; padding: 10px 16px; color: white; outline: none; font-size: 14px; }}

        /* STORY MODAL OVERLAY */
        .story-modal {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 2000; display: none; flex-direction: column; align-items: center; justify-content: center; padding: 20px; }}
        .story-modal.active {{ display: flex; }}
        .story-modal-img {{ max-width: 100%; max-height: 70vh; border-radius: 16px; object-fit: cover; margin-bottom: 15px; }}
        .story-modal-caption {{ font-size: 16px; text-align: center; color: #fff; font-weight: 600; margin-bottom: 20px; }}
        .close-modal-btn {{ position: absolute; top: 20px; right: 20px; color: #fff; font-size: 28px; cursor: pointer; }}
    </style>
</head>
<body>
    <div class="app-container">
        <!-- TOP HEADER -->
        <div class="top-header">
            <div class="app-logo"><i class="fa-solid fa-sparkles"></i> STATUS AI</div>
            <div class="energy-badge"><i class="fa-solid fa-bolt"></i> UNLIMITED ENERGY</div>
        </div>

        <!-- TAB 1: FEED -->
        <div id="tab-feed" class="tab-content active">
            <!-- STORIES BAR -->
            <div class="stories-section">
                <div class="stories-container">
                    <div class="story-item" onclick="openStory('{MEDIA_STUDIO}', 'Manager @gaerwenill on set! World tour prep in progress 🧭')">
                        <div class="story-ring my-story"><img src="{AVATAR_MANAGER}" class="story-avatar"></div>
                        <span class="story-username">Your Story</span>
                    </div>
                    <div class="story-item" onclick="openStory('{MEDIA_STUDIO}', 'Bang Chan: Late night studio recording session! STAYs listen closely 🎧❤️')">
                        <div class="story-ring"><img src="{AVATAR_CHAN}" class="story-avatar"></div>
                        <span class="story-username">gnabnahc</span>
                    </div>
                    <div class="story-item" onclick="openStory('{MEDIA_COOKIES}', 'Felix: Homemade brownies ready for @gaerwenill and 3RACHA! 🍪✨')">
                        <div class="story-ring"><img src="{AVATAR_FELIX}" class="story-avatar"></div>
                        <span class="story-username">yong.lixx</span>
                    </div>
                    <div class="story-item" onclick="openStory('{MEDIA_STUDIO}', 'Lee Know: Sooni, Doongi, Dori approved today choreo 🐱😏')">
                        <div class="story-ring"><img src="{AVATAR_LEEKNOW}" class="story-avatar"></div>
                        <span class="story-username">t.leeknow</span>
                    </div>
                    <div class="story-item" onclick="openStory('{MEDIA_STUDIO}', 'Hyunjin: New painting finished! Expressing my soul 🎨✨')">
                        <div class="story-ring"><img src="{AVATAR_HYUNJIN}" class="story-avatar"></div>
                        <span class="story-username">hynjinnnn</span>
                    </div>
                    <div class="story-item" onclick="openStory('{MEDIA_STUDIO}', 'Han Jisung: Wrote 3 songs in my sleep! You are welcome manager @gaerwenill 🎵')">
                        <div class="story-ring"><img src="{AVATAR_HAN}" class="story-avatar"></div>
                        <span class="story-username">_doolsetnet</span>
                    </div>
                </div>
            </div>

            <!-- CREATE POST -->
            <div class="create-post-box">
                <img src="{AVATAR_MANAGER}" class="post-avatar">
                <div style="flex:1; display:flex; flex-direction:column;">
                    <textarea id="new-post-text" class="create-post-input" placeholder="What's happening, Head Manager @gaerwenill?"></textarea>
                    <button class="publish-btn" onclick="publishPost()">Post</button>
                </div>
            </div>

            <!-- FEED POSTS -->
            <div class="feed" id="feed-posts">
                <!-- POST 1: BANG CHAN -->
                <div class="post">
                    <img src="{AVATAR_CHAN}" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Bang Chan</span> <i class="fa-solid fa-circle-check verified-badge"></i>
                            <span class="post-handle">@gnabnahc · 12m</span>
                        </div>
                        <div class="post-text">Huge shoutout to our head manager @gaerwenill for organizing everything for the upcoming world tour! STAYs, get ready! 🔥❤️</div>
                        <img src="{MEDIA_STUDIO}" class="post-image">
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 1,840</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 14.2K</span>
                            <span class="action-btn liked" onclick="toggleLike(this)"><i class="fa-solid fa-heart"></i> 68.5K</span>
                        </div>
                    </div>
                </div>

                <!-- POST 2: FELIX -->
                <div class="post">
                    <img src="{AVATAR_FELIX}" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Felix</span> <i class="fa-solid fa-circle-check verified-badge"></i>
                            <span class="post-handle">@yong.lixx · 35m</span>
                        </div>
                        <div class="post-text">Made a fresh batch of chocolate chip brownies for manager @gaerwenill and 3RACHA in the studio! Hope everyone stays warm and healthy today ✨🍪❤️</div>
                        <img src="{MEDIA_COOKIES}" class="post-image">
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 3,420</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 22.8K</span>
                            <span class="action-btn" onclick="toggleLike(this)"><i class="fa-regular fa-heart"></i> 112K</span>
                        </div>
                    </div>
                </div>

                <!-- POST 3: FAN ACCOUNT -->
                <div class="post">
                    <img src="{AVATAR_STAY}" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">STAY World Updates</span>
                            <span class="post-handle">@stay_updates · 1h</span>
                        </div>
                        <div class="post-text">WE LOVE YOU MANAGER @gaerwenill!! THANK YOU FOR ALWAYS PROTECTING STRAY KIDS AND WORKING SO HARD FOR US STAYs!! 😭😭💖💖 #ManagerGaerwenill #StrayKidsNextEra</div>
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 890</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 5,610</span>
                            <span class="action-btn" onclick="toggleLike(this)"><i class="fa-regular fa-heart"></i> 34.1K</span>
                        </div>
                    </div>
                </div>

                <!-- POST 4: DISPATCH -->
                <div class="post">
                    <img src="{AVATAR_DISPATCH}" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Dispatch Official</span> <i class="fa-solid fa-circle-check verified-badge"></i>
                            <span class="post-handle">@kpop_dispatch · 2h</span>
                        </div>
                        <div class="post-text">🚨 EXCLUSIVE: Stray Kids Head Manager @gaerwenill spotted arriving at JYP Center. Comeback album recording officially finalized?</div>
                        <img src="{MEDIA_DISPATCH}" class="post-image">
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 6,120</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 41.5K</span>
                            <span class="action-btn" onclick="toggleLike(this)"><i class="fa-regular fa-heart"></i> 189K</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 2: DMS -->
        <div id="tab-dms" class="tab-content">
            <div class="dm-header">
                <span>Direct Messages</span>
                <span style="font-size:12px; color:#a855f7; font-weight:600;"><i class="fa-solid fa-circle" style="font-size:8px; color:#22c55e;"></i> SKZ Online</span>
            </div>

            <!-- MEMBER SELECTOR -->
            <div class="dm-member-select">
                <div class="dm-member-card active" onclick="selectDMMember('Bang Chan', '@gnabnahc', '{AVATAR_CHAN}', this)">
                    <img src="{AVATAR_CHAN}" class="dm-member-avatar">
                    <span class="dm-member-name">Bang Chan</span>
                </div>
                <div class="dm-member-card" onclick="selectDMMember('Felix', '@yong.lixx', '{AVATAR_FELIX}', this)">
                    <img src="{AVATAR_FELIX}" class="dm-member-avatar">
                    <span class="dm-member-name">Felix</span>
                </div>
                <div class="dm-member-card" onclick="selectDMMember('Lee Know', '@t.leeknow', '{AVATAR_LEEKNOW}', this)">
                    <img src="{AVATAR_LEEKNOW}" class="dm-member-avatar">
                    <span class="dm-member-name">Lee Know</span>
                </div>
                <div class="dm-member-card" onclick="selectDMMember('Hyunjin', '@hynjinnnn', '{AVATAR_HYUNJIN}', this)">
                    <img src="{AVATAR_HYUNJIN}" class="dm-member-avatar">
                    <span class="dm-member-name">Hyunjin</span>
                </div>
            </div>

            <!-- CHAT CONTAINER -->
            <div class="chat-container" id="chat-box">
                <div class="chat-bubble incoming">
                    <div class="chat-sender" id="chat-sender-name">Bang Chan (@gnabnahc)</div>
                    Hey @gaerwenill! Thanks for checking in. We just finished recording the main vocal tracks for the new single. Do you have a moment to review tomorrow's photoshoot schedule?
                </div>
            </div>

            <!-- CHAT INPUT -->
            <div class="chat-input-bar">
                <input type="text" id="dm-input" class="chat-input" placeholder="Message as Head Manager @gaerwenill...">
                <button style="background:linear-gradient(135deg, #a855f7, #ec4899); color:white; border:none; padding:0 18px; border-radius:20px; font-weight:700; cursor:pointer;" onclick="sendDM()"><i class="fa-solid fa-paper-plane"></i></button>
            </div>
        </div>

        <!-- BOTTOM NAVIGATION -->
        <div class="bottom-nav">
            <div class="nav-item active" onclick="switchTab('feed', this)">
                <i class="fa-solid fa-house"></i>
                <span class="nav-label">Feed</span>
            </div>
            <div class="nav-item" onclick="switchTab('dms', this)">
                <i class="fa-solid fa-paper-plane"></i>
                <span class="nav-label">DMs</span>
            </div>
        </div>

        <!-- STORY MODAL OVERLAY -->
        <div class="story-modal" id="story-modal">
            <span class="close-modal-btn" onclick="closeStory()">&times;</span>
            <img src="" id="story-modal-img" class="story-modal-img">
            <div class="story-modal-caption" id="story-modal-caption"></div>
        </div>
    </div>

    <script>
        let currentMember = "Bang Chan";
        let currentHandle = "@gnabnahc";

        function switchTab(tabName, el) {{
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            el.classList.add('active');
        }}

        function toggleLike(btn) {{
            btn.classList.toggle('liked');
            let icon = btn.querySelector('i');
            if (btn.classList.contains('liked')) {{
                icon.className = 'fa-solid fa-heart';
            }} else {{
                icon.className = 'fa-regular fa-heart';
            }}
        }}

        function openStory(imgUrl, caption) {{
            document.getElementById('story-modal-img').src = imgUrl;
            document.getElementById('story-modal-caption').innerText = caption;
            document.getElementById('story-modal').classList.add('active');
        }}

        function closeStory() {{
            document.getElementById('story-modal').classList.remove('active');
        }}

        function publishPost() {{
            let input = document.getElementById('new-post-text');
            let text = input.value.trim();
            if (text !== '') {{
                let feed = document.getElementById('feed-posts');
                let newPostHTML = `
                <div class="post">
                    <img src="{AVATAR_MANAGER}" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">Gaerwenill</span> <i class="fa-solid fa-circle-check verified-badge"></i>
                            <span class="post-handle">@gaerwenill · Just now</span>
                        </div>
                        <div class="post-text">${{text}}</div>
                        <div class="post-actions">
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> 0</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> 0</span>
                            <span class="action-btn" onclick="toggleLike(this)"><i class="fa-regular fa-heart"></i> 1</span>
                        </div>
                    </div>
                </div>`;
                feed.insertAdjacentHTML('afterbegin', newPostHTML);
                input.value = '';

                setTimeout(() => {{
                    let memberResponses = [
                        {{ name: "Bang Chan", handle: "@gnabnahc", img: "{AVATAR_CHAN}", text: "Got it @gaerwenill! We are ready when you are 🔥❤️" }},
                        {{ name: "Felix", handle: "@yong.lixx", img: "{AVATAR_FELIX}", text: "Thank you manager @gaerwenill! Made brownies for everyone! ✨🍪" }}
                    ];
                    let resp = memberResponses[Math.floor(Math.random() * memberResponses.length)];
                    let commentHTML = `
                    <div class="post" style="background: rgba(168, 85, 247, 0.05);">
                        <img src="${{resp.img}}" class="post-avatar">
                        <div class="post-content">
                            <div class="post-header">
                                <span class="post-author">${{resp.name}}</span> <i class="fa-solid fa-circle-check verified-badge"></i>
                                <span class="post-handle">${{resp.handle}} · Replying to @gaerwenill</span>
                            </div>
                            <div class="post-text">${{resp.text}}</div>
                        </div>
                    </div>`;
                    feed.insertAdjacentHTML('afterbegin', commentHTML);
                }}, 1500);
            }}
        }}

        function selectDMMember(name, handle, avatar, el) {{
            document.querySelectorAll('.dm-member-card').forEach(card => card.classList.remove('active'));
            el.classList.add('active');
            currentMember = name;
            currentHandle = handle;
            document.getElementById('chat-sender-name').innerText = `${{name}} (${{handle}})`;

            let chatBox = document.getElementById('chat-box');
            let initialMsgs = {{
                'Bang Chan': "Hey @gaerwenill! Thanks for checking in. We just finished recording the main vocal tracks. Do you have a moment to review tomorrow's photoshoot schedule?",
                'Felix': "Hi manager @gaerwenill! I brought homemade cookies to the practice room. Should I save some for your office?",
                'Lee Know': "Manager @gaerwenill, did Changbin hyung tell you we need a protein break? Sooni, Doongi, and Dori miss me so I need to finish choreo early 😏",
                'Hyunjin': "The aesthetic of today's concept photos is incredible @gaerwenill! Did you see the lighting setup?"
            }};
            chatBox.innerHTML = `
            <div class="chat-bubble incoming">
                <div class="chat-sender">${{name}} (${{handle}})</div>
                ${{initialMsgs[name] || "Hey @gaerwenill! Ready for today's schedule!"}}
            </div>`;
        }}

        function sendDM() {{
            let input = document.getElementById('dm-input');
            let text = input.value.trim();
            if (text !== '') {{
                let chatBox = document.getElementById('chat-box');
                chatBox.innerHTML += `
                <div class="chat-bubble outgoing">
                    <div class="chat-sender">@gaerwenill</div>
                    ${{text}}
                </div>`;
                input.value = '';
                chatBox.scrollTop = chatBox.scrollHeight;

                setTimeout(() => {{
                    let memberReplies = {{
                        'Bang Chan': [
                            "I hear you @gaerwenill. I will make sure the boys rest before tomorrow morning's studio session. Thanks for looking out for us mate!",
                            "Awesome, I'll send the updated demo file to your email right away manager!"
                        ],
                        'Felix': [
                            "Thank you @gaerwenill!! You are the best manager ever! I'll make sure everyone drinks enough water during dance practice ❤️✨",
                            "Yay! I'll leave a box of brownies on your desk!"
                        ],
                        'Lee Know': [
                            "Understood @gaerwenill. Tell Changbin to stop being noisy during my cat pictures break 😏",
                            "Got it manager. Going back to dance practice now 🥩"
                        ],
                        'Hyunjin': [
                            "I'll prepare the outfit options for tomorrow's fitting @gaerwenill! Thanks for taking care of everything!",
                            "Dramatic? Me?! I am simply expressing my artistic soul manager! 🎨"
                        ]
                    }};
                    let replies = memberReplies[currentMember] || ["Got it manager @gaerwenill!"];
                    let randomReply = replies[Math.floor(Math.random() * replies.length)];

                    chatBox.innerHTML += `
                    <div class="chat-bubble incoming">
                        <div class="chat-sender">${{currentMember}} (${{currentHandle}})</div>
                        ${{randomReply}}
                    </div>`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                }}, 1200);
            }}
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=1000, scrolling=True)
""",TargetFile: