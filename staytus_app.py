import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Status AI - Stray Kids Edition",
    page_icon="✨",
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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Status AI - Stray Kids</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
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
            padding-bottom: 75px;
        }

        .top-header {
            position: sticky; top: 0; background: rgba(0, 0, 0, 0.92);
            backdrop-filter: blur(12px); z-index: 100; padding: 12px 16px;
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #16181c;
        }
        .app-logo {
            font-size: 20px; font-weight: 800;
            background: linear-gradient(45deg, #a855f7, #ec4899);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 6px;
        }
        .header-badge {
            font-size: 11px; font-weight: 700; color: #a855f7;
            background: rgba(168, 85, 247, 0.15); padding: 4px 10px;
            border-radius: 12px; border: 1px solid rgba(168, 85, 247, 0.3);
        }

        .stories-section {
            padding: 12px 0 8px 0; border-bottom: 1px solid #16181c; background: #000000;
        }
        .stories-title {
            font-size: 11px; font-weight: 700; color: #71767b; text-transform: uppercase;
            letter-spacing: 0.5px; padding: 0 16px 8px 16px;
        }
        .stories-container {
            display: flex; gap: 12px; padding: 0 16px; overflow-x: auto; scrollbar-width: none;
        }
        .stories-container::-webkit-scrollbar { display: none; }
        
        .story-item { display: flex; flex-direction: column; align-items: center; gap: 5px; cursor: pointer; flex-shrink: 0; }
        .story-ring {
            width: 64px; height: 64px; border-radius: 50%; padding: 2px;
            background: linear-gradient(45deg, #f09433, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888);
            display: flex; align-items: center; justify-content: center;
        }
        .story-avatar { width: 58px; height: 58px; border-radius: 50%; border: 2px solid #000; object-fit: cover; }
        .story-username { font-size: 11px; color: #e7e9ea; width: 66px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500; }

        .story-modal {
            display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0,0,0,0.95); z-index: 9999; justify-content: center; align-items: center;
        }
        .story-modal-content {
            width: 100%; max-width: 440px; height: 90vh; background: #111;
            border-radius: 16px; overflow: hidden; position: relative; display: flex;
            flex-direction: column; border: 1px solid #222;
        }
        .story-progress-bar {
            height: 3px; background: rgba(255,255,255,0.3); width: 94%; margin: 12px auto 0 auto;
            border-radius: 2px; overflow: hidden;
        }
        .story-progress-fill { height: 100%; background: #ffffff; width: 100%; transition: width 5s linear; }
        .story-modal-header {
            display: flex; justify-content: space-between; align-items: center;
            padding: 12px 16px; z-index: 10;
        }
        .story-author-info { display: flex; align-items: center; gap: 10px; }
        .story-modal-avatar { width: 36px; height: 36px; border-radius: 50%; object-fit: cover; border: 1px solid #fff; }
        .story-modal-name { font-weight: 700; font-size: 14px; color: #fff; }
        .story-close-btn { color: #fff; font-size: 22px; cursor: pointer; background: none; border: none; }
        .story-modal-img { width: 100%; flex: 1; object-fit: cover; }
        .story-modal-caption { padding: 16px; background: rgba(0,0,0,0.85); font-size: 15px; color: #fff; line-height: 1.4; }

        .composer-card {
            padding: 14px 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; background: #000;
        }
        .composer-avatar { width: 42px; height: 42px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
        .composer-right { flex: 1; display: flex; flex-direction: column; gap: 10px; }
        .composer-input {
            width: 100%; background: transparent; border: none; color: #e7e9ea;
            font-size: 15px; outline: none; resize: none; min-height: 48px;
        }
        .composer-footer { display: flex; justify-content: space-between; align-items: center; }
        .composer-btn {
            background: #a855f7; color: white; border: none; padding: 8px 18px;
            border-radius: 20px; font-weight: 700; font-size: 14px; cursor: pointer;
        }

        .feed { display: flex; flex-direction: column; }
        .post { padding: 16px; border-bottom: 1px solid #16181c; display: flex; gap: 12px; }
        .post-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
        .post-content { flex: 1; }
        .post-header { display: flex; align-items: center; gap: 4px; margin-bottom: 4px; }
        .post-author { font-weight: 700; font-size: 15px; color: #f7f9f9; }
        .verified-badge { color: #1d9bf0; font-size: 13px; margin-left: 2px; }
        .post-handle { color: #71767b; font-size: 14px; margin-left: 4px; }
        .post-text { font-size: 15px; line-height: 1.45; color: #e7e9ea; margin-bottom: 10px; white-space: pre-line; }
        .post-media { width: 100%; border-radius: 14px; margin-bottom: 10px; border: 1px solid #2f3336; max-height: 380px; object-fit: cover; }
        .post-actions { display: flex; justify-content: space-between; max-width: 320px; color: #71767b; font-size: 13px; margin-top: 6px; }
        .action-btn { display: flex; align-items: center; gap: 6px; cursor: pointer; background: none; border: none; color: #71767b; font-size: 13px; }

        .comments-section {
            margin-top: 12px; border-top: 1px solid #1f2328; padding-top: 10px; display: flex; flex-direction: column; gap: 10px;
        }
        .comment-item { display: flex; gap: 10px; font-size: 13.5px; line-height: 1.35; }
        .comment-avatar { width: 30px; height: 30px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
        .comment-body { background: #121417; padding: 8px 12px; border-radius: 12px; flex: 1; border: 1px solid #1c1f24; }
        .comment-author { font-weight: 700; color: #f7f9f9; margin-right: 4px; }
        .comment-handle { color: #71767b; font-size: 12px; }
        .comment-text { color: #d1d5db; margin-top: 2px; }

        .reply-box { display: flex; gap: 8px; margin-top: 8px; }
        .reply-input { flex: 1; background: #121417; border: 1px solid #22262c; border-radius: 18px; padding: 6px 14px; color: white; font-size: 13px; outline: none; }
        .reply-btn { background: #a855f7; color: #fff; border: none; padding: 6px 14px; border-radius: 18px; font-weight: 700; font-size: 12px; cursor: pointer; }

        .dm-header-list { padding: 12px 16px; border-bottom: 1px solid #16181c; font-weight: 800; font-size: 16px; color: #fff; }
        .dm-member-selector { display: flex; gap: 8px; padding: 10px 16px; overflow-x: auto; border-bottom: 1px solid #16181c; scrollbar-width: none; }
        .dm-member-chip {
            display: flex; align-items: center; gap: 8px; background: #121417; padding: 6px 12px;
            border-radius: 20px; border: 1px solid #22262c; cursor: pointer; flex-shrink: 0;
        }
        .dm-member-chip.active { background: #a855f7; border-color: #a855f7; color: white; }
        .dm-chip-avatar { width: 24px; height: 24px; border-radius: 50%; object-fit: cover; }
        .dm-chip-name { font-size: 13px; font-weight: 600; }

        .chat-container { padding: 16px; display: flex; flex-direction: column; gap: 12px; min-height: 380px; max-height: 520px; overflow-y: auto; }
        .chat-bubble { max-width: 82%; padding: 11px 15px; border-radius: 18px; font-size: 14px; line-height: 1.4; }
        .chat-bubble.incoming { background: #181a1f; color: #e7e9ea; align-self: flex-start; border-bottom-left-radius: 4px; border: 1px solid #22262c; }
        .chat-bubble.outgoing { background: #a855f7; color: white; align-self: flex-end; border-bottom-right-radius: 4px; }
        
        .chat-input-bar { position: fixed; bottom: 65px; width: 100%; max-width: 480px; background: #000; padding: 10px 16px; display: flex; gap: 10px; border-top: 1px solid #16181c; }
        .chat-input { flex: 1; background: #121417; border: 1px solid #22262c; border-radius: 20px; padding: 10px 16px; color: white; outline: none; font-size: 14px; }
        .chat-send-btn { background: #a855f7; color: white; border: none; padding: 0 18px; border-radius: 20px; font-weight: 700; cursor: pointer; }

        .bottom-nav {
            position: fixed; bottom: 0; width: 100%; max-width: 480px;
            background: rgba(0, 0, 0, 0.95); backdrop-filter: blur(12px);
            border-top: 1px solid #16181c; display: flex; justify-content: space-around;
            padding: 12px 0; z-index: 1000;
        }
        .nav-item { color: #71767b; font-size: 18px; text-decoration: none; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 3px; }
        .nav-item span { font-size: 10px; font-weight: 600; }
        .nav-item.active { color: #f7f9f9; }

        .tab-content { display: none; }
        .tab-content.active { display: block; }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="top-header">
            <div class="app-logo"><i class="fa-solid fa-sparkles"></i> Status</div>
            <div class="header-badge"><i class="fa-solid fa-bolt"></i> UNLIMITED ENERGY</div>
        </div>

        <div id="tab-feed" class="tab-content active">
            <div class="stories-section">
                <div class="stories-title">Recent Stories</div>
                <div class="stories-container" id="stories-list"></div>
            </div>

            <div class="composer-card">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80" class="composer-avatar">
                <div class="composer-right">
                    <textarea id="post-input" class="composer-input" placeholder="Publish update as Manager @gaerwenill..."></textarea>
                    <div class="composer-footer">
                        <span style="font-size: 12px; color: #71767b;">Head Manager</span>
                        <button class="composer-btn" onclick="addNewPost()">Post</button>
                    </div>
                </div>
            </div>

            <div class="feed" id="feed-posts"></div>
        </div>

        <div id="tab-dms" class="tab-content">
            <div class="dm-header-list">Direct Messages with Stray Kids</div>
            <div class="dm-member-selector" id="dm-selector"></div>
            <div class="chat-container" id="chat-box"></div>
            <div class="chat-input-bar">
                <input type="text" id="dm-input" class="chat-input" placeholder="Send message as @gaerwenill..." onkeypress="handleKeyPress(event)">
                <button class="chat-send-btn" onclick="sendDM()">Send</button>
            </div>
        </div>

        <div class="bottom-nav">
            <a class="nav-item active" onclick="switchTab('feed', this)">
                <i class="fa-solid fa-house"></i>
                <span>Feed</span>
            </a>
            <a class="nav-item" onclick="switchTab('dms', this)">
                <i class="fa-regular fa-paper-plane"></i>
                <span>Direct DMs</span>
            </a>
        </div>
    </div>

    <div class="story-modal" id="storyModal">
        <div class="story-modal-content">
            <div class="story-progress-bar"><div class="story-progress-fill" id="storyProgress"></div></div>
            <div class="story-modal-header">
                <div class="story-author-info">
                    <img id="modalAvatar" src="" class="story-modal-avatar">
                    <span id="modalName" class="story-modal-name"></span>
                </div>
                <button class="story-close-btn" onclick="closeStory()">&times;</button>
            </div>
            <img id="modalImg" src="" class="story-modal-img">
            <div class="story-modal-caption" id="modalCaption"></div>
        </div>
    </div>

    <script>
        const PHOTOS = {
            gaerwenill: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
            bangchan: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Bang_Chan_at_MLB_Event_in_October_2023.jpg/400px-Bang_Chan_at_MLB_Event_in_October_2023.jpg",
            leeknow: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Lee_Know_at_MLB_Event_in_October_2023.jpg/400px-Lee_Know_at_MLB_Event_in_October_2023.jpg",
            changbin: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Seo_Chang-bin_at_MLB_Event_in_October_2023.jpg/400px-Seo_Chang-bin_at_MLB_Event_in_October_2023.jpg",
            hyunjin: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Hwang_Hyun-jin_at_MLB_Event_in_October_2023.jpg/400px-Hwang_Hyun-jin_at_MLB_Event_in_October_2023.jpg",
            han: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Han_Ji-sung_at_MLB_Event_in_October_2023.jpg/400px-Han_Ji-sung_at_MLB_Event_in_October_2023.jpg",
            felix: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Felix_at_MLB_Event_in_October_2023.jpg/400px-Felix_at_MLB_Event_in_October_2023.jpg",
            seungmin: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Kim_Seung-min_at_MLB_Event_in_October_2023.jpg/400px-Kim_Seung-min_at_MLB_Event_in_October_2023.jpg",
            in: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Yang_Jeong-in_at_MLB_Event_in_October_2023.jpg/400px-Yang_Jeong-in_at_MLB_Event_in_October_2023.jpg",
            dispatch: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Dispatch_Korea_logo.svg/320px-Dispatch_Korea_logo.svg.png",
            jyp: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/JYP_Entertainment_Logo.svg/320px-JYP_Entertainment_Logo.svg.png",
            stay1: "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=200&q=80",
            stay2: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&q=80",
            stay3: "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=200&q=80",
            stay4: "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=200&q=80",
            stay5: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80",
            stay6: "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?auto=format&fit=crop&w=200&q=80",
            stage_photo: "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=800&q=80",
            studio_photo: "https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=800&q=80",
            cookies_photo: "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=800&q=80",
            dance_photo: "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?auto=format&fit=crop&w=800&q=80",
            news_photo: "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=800&q=80",
            art_photo: "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=800&q=80"
        };

        const SKZ_MEMBERS = [
            { id: "bangchan", name: "Bang Chan", handle: "@gnabnahc", photo: PHOTOS.bangchan },
            { id: "leeknow", name: "Lee Know", handle: "@t.leeknow", photo: PHOTOS.leeknow },
            { id: "changbin", name: "Changbin", handle: "@jutdwae", photo: PHOTOS.changbin },
            { id: "hyunjin", name: "Hyunjin", handle: "@hynjinnnn", photo: PHOTOS.hyunjin },
            { id: "han", name: "Han Jisung", handle: "@_doolsetnet", photo: PHOTOS.han },
            { id: "felix", name: "Felix", handle: "@yong.lixx", photo: PHOTOS.felix },
            { id: "seungmin", name: "Seungmin", handle: "@miniverse.___", photo: PHOTOS.seungmin },
            { id: "in", name: "I.N", handle: "@i.2.n.8", photo: PHOTOS.in }
        ];

        const STORIES = [
            { name: "Bang Chan", handle: "@gnabnahc", avatar: PHOTOS.bangchan, img: PHOTOS.studio_photo, caption: "Late night in 3RACHA studio working on track 4. Manager @gaerwenill approved the preliminary mix." },
            { name: "Felix", handle: "@yong.lixx", avatar: PHOTOS.felix, img: PHOTOS.cookies_photo, caption: "Freshly baked cookies ready for the members and Manager @gaerwenill before dance practice." },
            { name: "Lee Know", handle: "@t.leeknow", avatar: PHOTOS.leeknow, img: PHOTOS.dance_photo, caption: "Choreography rehearsal finished. 8 hours on stage today." },
            { name: "Hyunjin", handle: "@hynjinnnn", avatar: PHOTOS.hyunjin, img: PHOTOS.art_photo, caption: "Canvas completed between schedule hours. Art keeps the mind grounded." },
            { name: "Changbin", handle: "@jutdwae", avatar: PHOTOS.changbin, img: PHOTOS.studio_photo, caption: "Lyrical session done. 3RACHA producing era continues." },
            { name: "Han", handle: "@_doolsetnet", avatar: PHOTOS.han, img: PHOTOS.studio_photo, caption: "Working on new top lines with Chan hyung." },
            { name: "Seungmin", handle: "@miniverse.___", avatar: PHOTOS.seungmin, img: PHOTOS.dance_photo, caption: "Vocal rehearsal completed for the album track." },
            { name: "I.N", handle: "@i.2.n.8", avatar: PHOTOS.in, img: PHOTOS.stage_photo, caption: "Fitting for tomorrow's performance finished." },
            { name: "Dispatch", handle: "@kpop_dispatch", avatar: PHOTOS.dispatch, img: PHOTOS.news_photo, caption: "Dispatch Exclusive: Stray Kids schedule confirmed with Head Manager @gaerwenill." }
        ];

        let POSTS = [
            {
                id: 1,
                author: "Bang Chan",
                handle: "@gnabnahc",
                avatar: PHOTOS.bangchan,
                verified: true,
                time: "15m",
                text: "Full credit to our Head Manager @gaerwenill for coordinating the world tour logistics with JYP. Everything is running smoothly behind the scenes. STAY, get ready for the official announcement.",
                media: PHOTOS.stage_photo,
                likes: 54200,
                liked: false,
                comments: [
                    { name: "STAY Global News", handle: "@stay_updates", avatar: PHOTOS.stay1, text: "Thank you Manager @gaerwenill for taking such great care of the members during this busy era." },
                    { name: "Chan's Studio Fan", handle: "@chans_laptop", avatar: PHOTOS.stay2, text: "The leadership from Chan and Manager @gaerwenill is unmatched. We appreciate all the hard work." },
                    { name: "Tokyo STAY", handle: "@stay_tokyo_2026", avatar: PHOTOS.stay3, text: "Hoping Japan dates are included in the upcoming tour announcement." },
                    { name: "SKZ Chart Data", handle: "@skz_chart_data", avatar: PHOTOS.stay4, text: "Trending #1 worldwide: Manager Gaerwenill and Stray Kids World Tour." },
                    { name: "Felix Sunshine", handle: "@felix_brownie", avatar: PHOTOS.stay5, text: "Please make sure everyone gets enough rest between rehearsals." },
                    { name: "JYP Staff Team", handle: "@jyp_official_news", avatar: PHOTOS.jyp, text: "Logistics schedule verified by JYP Production Department." },
                    { name: "STAY Seoul", handle: "@skz_seoul", avatar: PHOTOS.stay6, text: "We trust Manager @gaerwenill completely." },
                    { name: "Australia STAY", handle: "@sydney_stay", avatar: PHOTOS.stay1, text: "Aussie line leading the team as always." },
                    { name: "3RACHA Beats", handle: "@3racha_fan", avatar: PHOTOS.stay2, text: "The new stage production is going to be massive." },
                    { name: "Han Jisung Fan", handle: "@han_quokka", avatar: PHOTOS.stay3, text: "Thank you for all the updates Manager @gaerwenill." }
                ]
            },
            {
                id: 2,
                author: "Felix",
                handle: "@yong.lixx",
                avatar: PHOTOS.felix,
                verified: true,
                time: "45m",
                text: "Baked two batches of chocolate chip cookies for Manager @gaerwenill and the 3RACHA team in the studio tonight. Stay warm everyone.",
                media: PHOTOS.cookies_photo,
                likes: 89400,
                liked: false,
                comments: [
                    { name: "Lee Know", handle: "@t.leeknow", avatar: PHOTOS.leeknow, text: "Save three for me or I am taking them tomorrow at the dance studio." },
                    { name: "Hyunjin", handle: "@hynjinnnn", avatar: PHOTOS.hyunjin, text: "They smelled amazing across the hallway." },
                    { name: "STAY Latam", handle: "@stay_latam", avatar: PHOTOS.stay6, text: "Felix is always the sweetest. Hope Manager @gaerwenill enjoyed them." },
                    { name: "Quokka Han", handle: "@han_jisung_fan", avatar: PHOTOS.stay1, text: "3RACHA was definitely motivated by those cookies while writing." },
                    { name: "Seungmin Doggo", handle: "@seungmin_fan", avatar: PHOTOS.stay2, text: "Felix baking era never fails us." },
                    { name: "IN Maknae", handle: "@i.2.n.8", avatar: PHOTOS.in, text: "Hyung save one for me please." },
                    { name: "Binnies Gym", handle: "@changbin_pigrabbit", avatar: PHOTOS.stay3, text: "Protein cookies next time Felix." },
                    { name: "STAY Europe", handle: "@stay_europe", avatar: PHOTOS.stay4, text: "Manager @gaerwenill is so well taken care of by the boys." }
                ]
            },
            {
                id: 3,
                author: "Dispatch Official",
                handle: "@kpop_dispatch",
                avatar: PHOTOS.dispatch,
                verified: true,
                time: "2h",
                text: "Dispatch Exclusive Report: Stray Kids Head Manager @gaerwenill arriving at JYPE Center for final album review meeting.",
                media: PHOTOS.news_photo,
                likes: 124000,
                liked: false,
                comments: [
                    { name: "K-Pop Insider", handle: "@kpop_insider", avatar: PHOTOS.stay3, text: "Manager @gaerwenill working overtime to ensure this comeback is seamless." },
                    { name: "STAY Protection", handle: "@protect_skz", avatar: PHOTOS.stay4, text: "Best manager team in the industry. Looking forward to the album drop." },
                    { name: "Binnies Gym", handle: "@changbin_pigrabbit", avatar: PHOTOS.stay5, text: "The production quality for this album is going to be insane." },
                    { name: "IN Maknae Fan", handle: "@jeongin_fox", avatar: PHOTOS.stay6, text: "We trust Manager @gaerwenill and SKZ completely." },
                    { name: "Dispatch Reporter", handle: "@dispatch_news", avatar: PHOTOS.dispatch, text: "Stay tuned for the official teaser schedule release." }
                ]
            }
        ];

        let CHATS = {
            bangchan: [
                { sender: "incoming", text: "Hey @gaerwenill. Vocal recording for track 3 is wrapped up. Do you have a moment to review tomorrow's photoshoot schedule?" }
            ],
            leeknow: [
                { sender: "incoming", text: "Manager @gaerwenill, dance practice finished early today. Are we confirmed for the 9 AM wardrobe fitting tomorrow?" }
            ],
            changbin: [
                { sender: "incoming", text: "Yo @gaerwenill! The verse for track 2 came out solid. Let me know when you listen to the audio file." }
            ],
            hyunjin: [
                { sender: "incoming", text: "Hi @gaerwenill! I sent over the concept sketches for the teaser photos. Let me know your thoughts whenever you are free." }
            ],
            han: [
                { sender: "incoming", text: "Manager @gaerwenill! Finished 2 new top-lines today. 3RACHA is ready for the tracklist meeting." }
            ],
            felix: [
                { sender: "incoming", text: "Hi @gaerwenill! I left a box of homemade cookies on your desk at JYPE. Thank you for coordinating everything today!" }
            ],
            seungmin: [
                { sender: "incoming", text: "Hello @gaerwenill. Vocal warm-up schedule for tomorrow is set. See you at the agency in the morning." }
            ],
            in: [
                { sender: "incoming", text: "Manager @gaerwenill! The outfit fitting went great. Ready for tomorrow's filming session!" }
            ]
        };

        let currentActiveDM = "bangchan";

        document.addEventListener("DOMContentLoaded", function() {
            renderStories();
            renderFeed();
            renderDMChips();
            loadChat(currentActiveDM);
        });

        function renderStories() {
            const container = document.getElementById("stories-list");
            let html = "";
            STORIES.forEach((s, idx) => {
                html += `
                <div class="story-item" onclick="openStory($${idx})">
                    <div class="story-ring">
                        <img src="${s.avatar}" class="story-avatar">
                    </div>
                    <span class="story-username">${s.name}</span>
                </div>
                `;
            });
            container.innerHTML = html;
        }

        function openStory(idx) {
            const s = STORIES[idx];
            document.getElementById("modalAvatar").src = s.avatar;
            document.getElementById("modalName").innerText = `${s.name} (${s.handle})`;
            document.getElementById("modalImg").src = s.img;
            document.getElementById("modalCaption").innerText = s.caption;
            
            document.getElementById("storyModal").style.display = "flex";
            const fill = document.getElementById("storyProgress");
            fill.style.width = "0%";
            setTimeout(() => { fill.style.width = "100%"; }, 50);
        }

        function closeStory() {
            document.getElementById("storyModal").style.display = "none";
        }

        function renderFeed() {
            const container = document.getElementById("feed-posts");
            let html = "";
            POSTS.forEach(post => {
                let commentsHtml = "";
                post.comments.forEach(c => {
                    commentsHtml += `
                    <div class="comment-item">
                        <img src="${c.avatar}" class="comment-avatar">
                        <div class="comment-body">
                            <span class="comment-author">${c.name}</span>
                            <span class="comment-handle">${c.handle}</span>
                            <div class="comment-text">${c.text}</div>
                        </div>
                    </div>
                    `;
                });

                html += `
                <div class="post">
                    <img src="${post.avatar}" class="post-avatar">
                    <div class="post-content">
                        <div class="post-header">
                            <span class="post-author">${post.author}</span>
                            ${post.verified ? '<i class="fa-solid fa-circle-check verified-badge"></i>' : ''}
                            <span class="post-handle">${post.handle} · ${post.time}</span>
                        </div>
                        <div class="post-text">${post.text}</div>
                        ${post.media ? `<img src="${post.media}" class="post-media">` : ''}
                        
                        <div class="post-actions">
                            <button class="action-btn" onclick="toggleLike(${post.id}, this)">
                                <i class="${post.liked ? 'fa-solid' : 'fa-regular'} fa-heart" style="${post.liked ? 'color:#f91880;' : ''}"></i>
                                <span>${post.likes.toLocaleString()}</span>
                            </button>
                            <span class="action-btn"><i class="fa-regular fa-comment"></i> ${post.comments.length}</span>
                            <span class="action-btn"><i class="fa-solid fa-retweet"></i> Share</span>
                        </div>

                        <div class="comments-section">
                            ${commentsHtml}
                            <div class="reply-box">
                                <input type="text" id="reply-input-${post.id}" class="reply-input" placeholder="Comment as Manager @gaerwenill...">
                                <button class="reply-btn" onclick="addComment(${post.id})">Reply</button>
                            </div>
                        </div>
                    </div>
                </div>
                `;
            });
            container.innerHTML = html;
        }

        function toggleLike(postId, btn) {
            const post = POSTS.find(p => p.id === postId);
            if (post) {
                post.liked = !post.liked;
                post.likes += post.liked ? 1 : -1;
                renderFeed();
            }
        }

        function addComment(postId) {
            const input = document.getElementById(`reply-input-${postId}`);
            if (input && input.value.trim() !== "") {
                const post = POSTS.find(p => p.id === postId);
                if (post) {
                    post.comments.push({
                        name: "Gaerwenill",
                        handle: "@gaerwenill",
                        avatar: PHOTOS.gaerwenill,
                        text: input.value.trim()
                    });
                    
                    setTimeout(() => {
                        const botReplies = [
                            { name: "Bang Chan", handle: "@gnabnahc", avatar: PHOTOS.bangchan, text: "Acknowledged Manager @gaerwenill. We will follow this schedule." },
                            { name: "Felix", handle: "@yong.lixx", avatar: PHOTOS.felix, text: "Thank you for coordinating Manager @gaerwenill." },
                            { name: "STAY Updates", handle: "@stay_updates", avatar: PHOTOS.stay1, text: "Thank you Manager @gaerwenill for keeping STAY updated." }
                        ];
                        const randomBot = botReplies[Math.floor(Math.random() * botReplies.length)];
                        post.comments.push(randomBot);
                        renderFeed();
                    }, 1000);

                    renderFeed();
                }
            }
        }

        function addNewPost() {
            const text = document.getElementById("post-input").value;
            if (text.trim() !== "") {
                const newPostObj = {
                    id: Date.now(),
                    author: "Gaerwenill",
                    handle: "@gaerwenill",
                    avatar: PHOTOS.gaerwenill,
                    verified: true,
                    time: "Just now",
                    text: text.trim(),
                    media: null,
                    likes: 1240,
                    liked: false,
                    comments: [
                        { name: "Bang Chan", handle: "@gnabnahc", avatar: PHOTOS.bangchan, text: "Received Manager @gaerwenill. I will inform the rest of 3RACHA immediately." },
                        { name: "Felix", handle: "@yong.lixx", avatar: PHOTOS.felix, text: "Thank you @gaerwenill. We are preparing for practice now." },
                        { name: "STAY World", handle: "@stay_updates", avatar: PHOTOS.stay2, text: "Official update confirmed by Head Manager @gaerwenill." }
                    ]
                };
                POSTS.unshift(newPostObj);
                document.getElementById("post-input").value = "";
                renderFeed();
            }
        }

        function renderDMChips() {
            const container = document.getElementById("dm-selector");
            let html = "";
            SKZ_MEMBERS.forEach(m => {
                const active = m.id === currentActiveDM ? "active" : "";
                html += `
                <div class="dm-member-chip ${active}" onclick="selectDM('${m.id}')">
                    <img src="${m.photo}" class="dm-chip-avatar">
                    <span class="dm-chip-name">${m.name}</span>
                </div>
                `;
            });
            container.innerHTML = html;
        }

        function selectDM(memberId) {
            currentActiveDM = memberId;
            renderDMChips();
            loadChat(memberId);
        }

        function loadChat(memberId) {
            const chatBox = document.getElementById("chat-box");
            const member = SKZ_MEMBERS.find(m => m.id === memberId);
            const messages = CHATS[memberId] || [];

            let html = "";
            messages.forEach(msg => {
                if (msg.sender === "incoming") {
                    html += `
                    <div class="chat-bubble incoming">
                        <strong style="color:#a855f7; font-size:12px;">${member.name} (${member.handle})</strong><br>
                        ${msg.text}
                    </div>
                    `;
                } else {
                    html += `
                    <div class="chat-bubble outgoing">
                        <strong style="color:#e9d5ff; font-size:12px;">@gaerwenill</strong><br>
                        ${msg.text}
                    </div>
                    `;
                }
            });
            chatBox.innerHTML = html;
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function sendDM() {
            const input = document.getElementById("dm-input");
            const text = input.value.trim();
            if (text !== "") {
                if (!CHATS[currentActiveDM]) CHATS[currentActiveDM] = [];
                CHATS[currentActiveDM].push({ sender: "outgoing", text: text });
                input.value = "";
                loadChat(currentActiveDM);

                setTimeout(() => {
                    const responses = {
                        bangchan: "Understood @gaerwenill. I will go over the details with the team during dinner.",
                        leeknow: "Got it Manager @gaerwenill. I am heading to the practice room now.",
                        changbin: "Sounds good @gaerwenill! I will double check the vocal tracks before tomorrow.",
                        hyunjin: "Thank you Manager @gaerwenill. I will be ready on time for the photoshoot.",
                        han: "Perfect @gaerwenill. 3RACHA is on it.",
                        felix: "Thank you so much Manager @gaerwenill. Have a wonderful rest of your evening!",
                        seungmin: "Understood @gaerwenill. Vocal rehearsal is logged for 10 AM.",
                        in: "Got it Manager @gaerwenill! Thank you!"
                    };
                    const replyText = responses[currentActiveDM] || "Understood Manager @gaerwenill.";
                    CHATS[currentActiveDM].push({ sender: "incoming", text: replyText });
                    loadChat(currentActiveDM);
                }, 1000);
            }
        }

        function handleKeyPress(e) {
            if (e.key === "Enter") {
                sendDM();
            }
        }

        function switchTab(tabName, el) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            document.getElementById('tab-' + tabName).classList.add('active');
            el.classList.add('active');
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
