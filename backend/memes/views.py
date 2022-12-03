from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import spacy
import re
import json
import os
from .models import Subscribers
from django.http import JsonResponse

return_data = {
    "data": [
        {
            "news_name": "What we know about the victims of the LGBTQ+ nightclub shooting so far",
            "news_url": "https://www.msn.com/en-us/news/crime/what-we-know-about-the-victims-of-the-lgbtq-nightclub-shooting-so-far/ar-AA14l2B7",
            "news_description": "  A bartender was one of the victims killed in a mass shooting at an LGBTQ+ nightclub in Colorado late Saturday night, ABC News has learned.   Five people were killed and 25 were injured after a",
            "meme_urls": [
                "https://i.imgflip.com/71h15l.jpg",
                "https://i.imgflip.com/71golt.png",
                "https://i.imgflip.com/71g93e.jpg",
                "https://i.redd.it/fd2m122k611a1.jpg",
                "https://i.imgflip.com/71gxvc.jpg",
                "https://preview.redd.it/brb-processing-the-latest-traumatic-news-via-memes-v0-j843ezbxj71a1.jpg?auto=webp&s=e750b6b4583daabdcb43cabba2e091723d051c38",
                "https://preview.redd.it/aj1clc5u971a1.png?width=640&crop=smart&auto=webp&s=47f438593b2681fb4d99f2b4be634abef8ea497c",
                "https://i.redd.it/bh5kk8uhcz0a1.jpg",
                "https://i.imgflip.com/71fubn.jpg",
                "https://i.redd.it/djlem6pld31a1.jpg"
            ]
        },
        {
            "news_name": "Club Q 'heroic customers' subdued gunman and saved lives, officials say",
            "news_url": "https://www.msn.com/en-us/news/us/club-q-heroic-customers-subdued-gunman-and-saved-lives-officials-say/ar-AA14kCHt",
            "news_description": "Two people subdued the gunman who opened fire at Club Q, a Colorado Springs LGBTQ nightclub late on Saturday, saving lives, officials say.\"While the suspect was inside of the club, at least two",
            "meme_urls": [
                "https://s.yimg.com/ny/api/res/1.2/Vr0xuYIGnSGYDj8V2RfrKA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTcwNTtoPTM5Nw--/https://media.zenfs.com/en/the_advocate_articles_932/0ac596fd09efe833b1c131c91a6261b9",
                "https://kdvr.com/wp-content/uploads/sites/11/2022/11/316431572_518295673532316_5772350013765134402_n-e1668968014994.jpg?w=1440&h=870&crop=1",
                "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA14kUOd.img?h=0&w=600&m=6&q=60&u=t&o=f&l=f",
                "https://ic-cdn.flipboard.com/advocate.com/284f7290dda27377eeab8788c467bc61b2423af2/_medium.jpeg",
                "https://cdn.bolnews.com/wp-content/uploads/2022/11/FotoJet-13-74.jpg",
                "https://media.kompas.tv/library/image/content_article/article_img/20221120152238.jpg",
                "https://pyxis.nymag.com/v1/imgs/055/042/fa552eeb3c1eab67b319260f18e3c3ec2c-club-q-nightclub-attack.1x.rsocial.w1200.jpg",
                "https://gray-wsmv-prod.cdn.arcpublishing.com/resizer/7XMZX8u9a7HvyIv7qDLcIIuwP7Q=/1200x1800/smart/filters:quality(85)/do0bihdskp9dy.cloudfront.net/11-20-2022/t_ae29c3a1c24a4ba285668bffde2f0c1d_name_file_1280x720_2000_v3_1_.jpg",
                "https://img.i-scmp.com/cdn-cgi/image/fit=contain,width=1098,format=auto/sites/default/files/styles/1200x800/public/d8/images/canvas/2022/11/21/6cdf0a72-a958-40c1-ac28-6ed7d39a0421_b7f41e54.jpg?itok=PE-JDYfS&v=1668976568",
                "https://www.siouxlandproud.com/wp-content/uploads/sites/68/2022/11/Club-Q-shooting.png?w=600&h=600&crop=1"
            ]
        },
        {
            "news_name": "Shells hit near nuclear plant; Blackouts roll across Ukraine",
            "news_url": "https://www.msn.com/en-us/news/world/shells-hit-near-nuclear-plant-blackouts-roll-across-ukraine/ar-AA14kvOS",
            "news_description": "KYIV, Ukraine (AP) — Powerful explosions from shelling shook Ukraine's Zaporizhzhia region, the site of Europe's largest nuclear power plant, the global nuclear watchdog said Sunday, calling for",
            "meme_urls": [
                "https://pbs.twimg.com/media/FiCSxdkWAAEvNPo?format=jpg&name=4096x4096",
                "https://preview.redd.it/7oi1kb7yt51a1.jpg?auto=webp&s=8be05e80112b5b30b89180b08aa9778ab0a86087",
                "https://images3.memedroid.com/images/UPLOADED756/637a62d7a5f7d.jpeg",
                "https://img-9gag-fun.9cache.com/photo/ay2D9DX_460s.jpg",
                "https://pbs.twimg.com/media/FiBkOzyWYAUJbtL.jpg",
                "https://i.kym-cdn.com/photos/images/original/002/481/743/bb0.jpg",
                "https://i.redd.it/t6adjqcvi11a1.jpg",
                "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/8ba63e3939904c9f9a885b4a8d718abe_1668008219~tplv-tiktokx-share-play.jpeg?x-expires=1669550400&x-signature=8filTq7kwbzdqeMa8nY4u6AgfII%3D",
                "https://www.tiktok.com/api/img/?itemId=7168194106370411782&location=0&aid=1988",
                "https://i.kym-cdn.com/photos/images/newsfeed/002/481/569/0d1.jpg"
            ]
        },
        {
            "news_name": "5 migrants dead, 5 missing after boat capsizes off coast of Florida",
            "news_url": "https://www.msn.com/en-us/news/us/5-migrants-dead-5-missing-after-boat-capsizes-off-coast-of-florida/ar-AA14li5s",
            "news_description": "  Five migrants have died and another five are missing after a boat capsized off the coast of Florida, the US Coast Guard said in a statement.   A group of migrants was traveling in a homemade boat",
            "meme_urls": [
                "https://images3.memedroid.com/images/UPLOADED775/63794ce6a99d0.jpeg",
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=674891083996945",
                "https://preview.redd.it/nice-chase-tho-v0-bv6lr7exd61a1.gif?format=png8&s=409b653168ecefffec1d129e8ce1839e1ad3d06e",
                "https://on3static.com/xf/data/attachments/264/264751-2964976e0bc68eeac816ebed93a80215.jpg",
                "https://i.kym-cdn.com/photos/images/original/002/481/502/a1c.png",
                "https://i.ytimg.com/vi/gTmYf1LC7OU/sddefault.jpg",
                "https://pbs.twimg.com/media/FiAw4ozXkAM7qhi.jpg",
                "https://i.imgflip.com/71i6uh.jpg",
                "http://images7.memedroid.com/images/UPLOADED505/63797a1977aa3.jpeg",
                "https://i.redd.it/c3cgucxo021a1.png"
            ]
        },
        {
            "news_name": "Gay club shooting suspect evaded Colorado's red flag gun law",
            "news_url": "https://www.msn.com/en-us/news/us/gay-club-shooting-suspect-evaded-colorados-red-flag-gun-law/ar-AA14llJG",
            "news_description": "DENVER (AP) — A year and a half before he was arrested in the Colorado Springs gay nightclub shooting that left five people dead, Anderson Lee Aldrich allegedly threatened his mother with a homemade",
            "meme_urls": [
                "https://images3.memedroid.com/images/UPLOADED863/637a5d236e0b4.jpeg",
                "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/6e5d00c2ed5e426e9224ec4c75c48353_1662034036~tplv-tiktokx-share-play.jpeg?x-expires=1669518000&x-signature=Tl0CjsfEW%2BcB8lCZvXYpkjAkpaY%3D",
                "https://images.hola.com/us/images/025c-0f221d8af5f3-46ece328bdb2-1000/horizontal-800/extrovert-memes.jpg",
                "https://preview.redd.it/s11urw1f521a1.gif?format=png8&s=e95240b27b115bcfcf44073438b271a9c79cd2fa",
                "https://img.ifunny.co/images/4da82367b4757d0297cdfc950205fab3585e47e677b36352cb296d479dcb63c6_1.jpg",
                "https://kdvr.com/wp-content/uploads/sites/11/2022/11/Club-Q-Memorial-Colorado-Springs-e1668967327224.jpg?w=1920&h=1080&crop=1",
                "https://www.bostonglobe.com/resizer/iICDAKe4ltN8pgfC41POke-EnZg=/cloudfront-us-east-1.images.arcpublishing.com/bostonglobe/DBPD7XYJ5OFOMY7WFEML2HLFZA.jpg",
                "https://images3.memedroid.com/images/UPLOADED909/637a09f8a41de.jpeg",
                "https://preview.redd.it/youre-just-gonna-have-to-respawn-at-the-bed-v0-wjgik7xbk21a1.png?auto=webp&s=4739470866a4c0e50e1091dc7c7b90f7d09f31d4",
                "https://pbs.twimg.com/media/FiBQOOSUAAA84rT?format=jpg&name=large"
            ]
        },
        {
            "news_name": "Elton John bids farewell to America from Dodger Stadium: What to know, where to watch his final show",
            "news_url": "https://www.msn.com/en-us/music/news/elton-john-bids-farewell-to-america-from-dodger-stadium-what-to-know-where-to-watch-his-final-show/ar-AA14lzHF",
            "news_description": "LOS ANGELES —  The sun is setting on Elton John's final North American show in the place where it all began – Dodger Stadium.             John, 75, will close out his Goodbye Yellow Brick Road tour,",
            "meme_urls": [
                "https://us.knews.media/wp-content/uploads/2022/11/Collage-Maker-14-Oct-2022-0340-PM-780x470.jpg",
                "https://img.ifunny.co/images/e3b8fbacda6825c216ab00077121e5a0913c0fa9434c8ad1b310c62c545e1136_1.jpg",
                "https://deadline.com/wp-content/uploads/2022/11/elton-john.jpg?w=200&h=112&crop=1",
                "https://www.informador.mx/__export/1668802862624/sites/elinformador/img/2022/11/18/elton_john_live_1_1_crop1668802796449.jpg_423682103.jpg",
                "https://pbs.twimg.com/media/Fh-7gs5XkAA5bag.jpg",
                "https://www.informador.mx/__export/1668802728402/sites/elinformador/img/2022/11/18/elton_john_live_1_crop1668802727609.jpg_524400468.jpg",
                "https://pbs.twimg.com/media/Fh2zPZZX0AUVDka.jpg",
                "https://static1.srcdn.com/wordpress/wp-content/uploads/2022/10/tumblr_0f35d3e1a0c276895cb0c7168dab3edb_a8978c27_1280.png",
                "https://pbs.twimg.com/media/FiB86J9aYAAd1m-.jpg",
                "https://townsquare.media/site/295/files/2022/11/attachment-2022GiftGuide.jpg",
                "https://img-9gag-fun.9cache.com/photo/a6qbN2q_460s.jpg",
                "https://i.imgflip.com/71gkrp.jpg",
                "https://i.imgflip.com/71gn5q.jpg",
                "https://i.imgflip.com/70krdb.jpg",
                "https://external-preview.redd.it/XOdZBbHHHEJdnl_yDP6HFra1Lmo2QdniBQAGt_0LSeo.png?format=pjpg&auto=webp&s=75bf0d49aa58a2c62275358caeea06fe3a575935",
                "https://i.kym-cdn.com/photos/images/original/002/481/768/abf.jpg",
                "https://img.ifunny.co/images/e10da8602f96db5958f72d0afca34a36624ed460974fa27f73203fbbdc3c19e5_1.jpg",
                "https://img.ifunny.co/images/23d889cabc5b891c6a462b5d4e6c29ba473916f5d97fa7d4b308fd0416ba2395_3.jpg",
                "https://i.imgflip.com/71i5dg.jpg",
                "https://preview.redd.it/0lnkw0cwq71a1.jpg?width=640&crop=smart&auto=webp&s=fc20f2bea270869550ace09ff2b8ba9e5db36dbf",
                "https://i.imgur.com/SpmaYnt.jpg",
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=510897607437119&get_thumbnail=1",
                "https://img.mlbstatic.com/mlb-images/image/upload/t_16x9/t_w1536/mlb/ih6oa7wmbbygj3w5vlyj.jpg",
                "https://cloudfront-us-east-1.images.arcpublishing.com/cmg/GRKDAG4MXT37HLEQNZRP7XMSFY.jpg",
                "https://pbs.twimg.com/media/FiBpfgBUYAEjQ3o?format=jpg&name=large",
                "https://cdn.abcotvs.com/dip/images/12473950_111922-kabc-11pm-dodger-stadium-attack-vid.jpg?w=660&r=16%3A9",
                "https://cdn.vox-cdn.com/thumbor/d0JW7_KvSZ7QNwHUeH1WW8pL4no=/0x0:4014x2676/1200x800/filters:focal(921x197:1563x839)/cdn.vox-cdn.com/uploads/chorus_image/image/71652691/1432728647.0.jpg",
                "https://pbs.twimg.com/media/Fh-o7nqXoAA1KBY.jpg",
                "https://ca-times.brightspotcdn.com/dims4/default/4c1e38c/2147483647/strip/true/crop/6344x4680+0+0/resize/1200x885!/quality/80/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F6a%2F10%2Ffd970c7a4f14a5c62ee7f14b3878%2F1216508-sp-1119-usc-ucla-football8-wjs.jpg",
                "https://pbs.twimg.com/media/FiCKk2qUoAAynyE.jpg"
            ]
        },
        {
            "news_name": "Club Q shooting follows year of bomb threats, drag protests, anti-trans bills",
            "news_url": "https://www.msn.com/en-us/news/us/club-q-shooting-follows-year-of-bomb-threats-drag-protests-anti-trans-bills/ar-AA14l2P3",
            "news_description": "   In the hours after the shooting, investigators did not say what led someone to open fire Saturday night in a Colorado gay bar, killing at least five people and injuring 25 others. But LGBTQ",
            "meme_urls": [
                "https://s.yimg.com/ny/api/res/1.2/Vr0xuYIGnSGYDj8V2RfrKA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTcwNTtoPTM5Nw--/https://media.zenfs.com/en/the_advocate_articles_932/0ac596fd09efe833b1c131c91a6261b9",
                "https://kdvr.com/wp-content/uploads/sites/11/2022/11/316431572_518295673532316_5772350013765134402_n-e1668968014994.jpg?w=1440&h=870&crop=1",
                "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA14kUOd.img?h=0&w=600&m=6&q=60&u=t&o=f&l=f",
                "https://ic-cdn.flipboard.com/advocate.com/284f7290dda27377eeab8788c467bc61b2423af2/_medium.jpeg",
                "https://cdn.bolnews.com/wp-content/uploads/2022/11/FotoJet-13-74.jpg",
                "https://media.kompas.tv/library/image/content_article/article_img/20221120152238.jpg",
                "https://pyxis.nymag.com/v1/imgs/055/042/fa552eeb3c1eab67b319260f18e3c3ec2c-club-q-nightclub-attack.1x.rsocial.w1200.jpg",
                "https://gray-wsmv-prod.cdn.arcpublishing.com/resizer/7XMZX8u9a7HvyIv7qDLcIIuwP7Q=/1200x1800/smart/filters:quality(85)/do0bihdskp9dy.cloudfront.net/11-20-2022/t_ae29c3a1c24a4ba285668bffde2f0c1d_name_file_1280x720_2000_v3_1_.jpg",
                "https://img.i-scmp.com/cdn-cgi/image/fit=contain,width=1098,format=auto/sites/default/files/styles/1200x800/public/d8/images/canvas/2022/11/21/6cdf0a72-a958-40c1-ac28-6ed7d39a0421_b7f41e54.jpg?itok=PE-JDYfS&v=1668976568",
                "https://www.siouxlandproud.com/wp-content/uploads/sites/68/2022/11/Club-Q-shooting.png?w=600&h=600&crop=1"
            ]
        },
        {
            "news_name": "'Historic' storm: Snow eases in parts of New York, but travel remains treacherous for some",
            "news_url": "https://www.msn.com/en-us/weather/topstories/historic-storm-snow-eases-in-parts-of-new-york-but-travel-remains-treacherous-for-some/ar-AA14kIBL",
            "news_description": "The fierce storm that pounded parts of New York with prodigious snow totals finally relented in the most affected areas Sunday, but it was expected to bring treacherous travel conditions to",
            "meme_urls": [
                "https://i.redd.it/es3pnrcph41a1.png",
                "https://i.imgflip.com/71f5ov.jpg",
                "https://i.imgflip.com/71fioo.jpg",
                "https://preview.redd.it/4qfxjfaxx51a1.jpg?auto=webp&s=7f21218e592876afb2635d0ec0557ec5fad83137",
                "https://i.kym-cdn.com/photos/images/newsfeed/002/481/570/a5d.png",
                "https://images3.memedroid.com/images/UPLOADED328/637926fea6fcb.jpeg",
                "https://i.kym-cdn.com/photos/images/facebook/002/481/710/91e.jpg",
                "https://img.ifunny.co/images/2733298f00917a73bf1b99f6acdf88f62c684364a298e34fda2f6c989003e3a5_1.jpg",
                "https://i.redd.it/6wl691s2r31a1.jpg",
                "https://img-9gag-fun.9cache.com/photo/aNwA0nw_460s.jpg",
                "https://images7.memedroid.com/images/UPLOADED735/63799858794e5.jpeg",
                "https://img.ifunny.co/images/57feb6704a7d9e2f7bae3409b42f04ef5dbae19ee46459b671981bf54c1d9d09_1.jpg",
                "https://p16-sign-va.tiktokcdn.com/obj/tos-maliva-p-0068/d2a92bd440f14450872fc9e9c96992a5_1579475546?x-expires=1668996000&x-signature=o8Yp07023Q1zgpw1dd%2FB1CkOxW0%3D",
                "https://i.kym-cdn.com/photos/images/masonry/002/481/619/4bc.gif",
                "https://i.redd.it/nhjzx37er01a1.png",
                "https://www.guide4moms.com/wp-content/uploads/2021/01/Inauguration-Day-Memes-15.jpg.webp",
                "https://img.ifunny.co/images/399b7b0ebfc04223376a51830cd105a344e442675b712abbfbd494479848061b_1.jpg",
                "https://i.chzbgr.com/thumb800/18474245/hE79ED038/funny-memes",
                "https://preview.redd.it/p7iszsn4441a1.jpg?auto=webp&s=8f7d0df91109c5e6b429899848114a731907b762",
                "https://us.knews.media/wp-content/uploads/2022/11/Collage-Maker-14-Oct-2022-0340-PM-780x470.jpg"
            ]
        },
        {
            "news_name": "World still ‘on brink of climate catastrophe’ after Cop27 deal",
            "news_url": "https://www.msn.com/en-us/news/world/world-still-on-brink-of-climate-catastrophe-after-cop27-deal/ar-AA14l631",
            "news_description": " The world still stands “on the brink of climate catastrophe” after the deal reached at the Cop27 UN climate summit on Sunday, and the biggest economies must make fresh commitments to cut greenhouse",
            "meme_urls": [
                "https://images3.memedroid.com/images/UPLOADED117/637a34aa51069.jpeg",
                "https://preview.redd.it/55wefxgpz21a1.jpg?auto=webp&s=a18a6d82c69d3f0211af985a25e410cdbc6e06d8",
                "https://i.kym-cdn.com/photos/images/facebook/002/481/567/113.jpg",
                "https://preview.redd.it/i-bet-china-will-love-this-movie-v0-k1i4ax6gf71a1.jpg?auto=webp&s=99cbb6d952a45427290f8f6274b1d20880a24feb",
                "https://i.imgflip.com/71f5ov.jpg",
                "https://i.kym-cdn.com/photos/images/newsfeed/002/481/596/3cf.jpg",
                "https://i.kym-cdn.com/photos/images/original/002/481/861/728.jpg",
                "https://external-preview.redd.it/F3SJhMDOiXRK9V9nnlrDlJz1naAWlaIwtG02AyPazos.png?width=640&crop=smart&format=pjpg&auto=webp&s=dfcfdcabcd2ae724b43d56c2fb866398a19d7fcf",
                "https://i.imgflip.com/71ivxc.jpg",
                "https://st1.latestly.com/wp-content/uploads/2022/11/JioCinema-Posts-Funny-Meme-380x214.jpg",
                "https://www.reuters.com/resizer/9aecadYA91oK91rmbKUOjqIGsgM=/960x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/63QF2LVED5IVHBZVFTHHE4BYCY.jpg",
                "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA14k7fb.img?m=6&q=80",
                "https://pbs.twimg.com/media/Fh_gGFcWQAIZ5nH.jpg",
                "https://i.redd.it/3j16yn34441a1.jpg",
                "https://img.ifunny.co/images/85d8eb34a47c5d9c90f8d109d80fdf736947cac59a83937f139dc89d2eb80656_1.jpg",
                "https://e3.365dm.com/22/11/1600x900/skynews-cop27-egypt_5971957.jpg?20221120073931",
                "https://img.i-scmp.com/cdn-cgi/image/fit=contain,width=1098,format=auto/sites/default/files/styles/1200x800/public/d8/images/canvas/2022/11/20/bda65c5d-0f5d-4fbb-902e-7b70ae6e9060_a9e780e8.jpg?itok=DB-Olg9F&v=1668939756",
                "https://www.chiangraitimes.com/wp-content/uploads/2022/11/Countries-Adopt-COP27-Deal-With-Loss-and-Damage-Fund-in-Overnight-Session-1000x600.webp",
                "https://pbs.twimg.com/card_img/1594298580239425536/VUD8xx63?format=jpg&name=medium",
                "https://media1.ledevoir.com/documents/image/article_sujets/637aa1850987b.jpg"
            ]
        },
        {
            "news_name": "As Biden turns 80, Americans ask 'What's too old?'",
            "news_url": "https://www.msn.com/en-us/news/politics/as-biden-turns-80-americans-ask-whats-too-old/ar-AA14k3f1",
            "news_description": "By Steve Holland and Jason LangeWASHINGTON (Reuters) -   Joe Biden turns 80 on Sunday, making him the first octogenarian president in U.S. history.He is set to celebrate his birthday with a brunch",
            "meme_urls": [
                "https://i.imgflip.com/71f95v.jpg",
                "https://i.imgflip.com/71ipgq.jpg",
                "https://i.imgflip.com/71fykv.jpg",
                "https://i.imgflip.com/71i04l.jpg",
                "https://freebeacon.com/wp-content/uploads/2022/11/biden-birthday-final.png",
                "https://i2-prod.mirror.co.uk/incoming/article28540237.ece/ALTERNATES/s615b/0_biden.jpg",
                "https://i.imgflip.com/71ijhv.jpg",
                "https://i.imgflip.com/6znr42.jpg",
                "https://i.imgflip.com/71hgjz.jpg",
                "https://www.tiktok.com/api/img/?itemId=7167962350669024558&location=0&aid=1988",
                "https://img-9gag-fun.9cache.com/photo/a6qbN2q_460s.jpg",
                "https://i.imgflip.com/71gn5q.jpg",
                "https://i.redd.it/urp9zo4s041a1.jpg",
                "https://i.redd.it/uadtcc1qy51a1.jpg",
                "https://img.ifunny.co/images/cf9635ab2ce9f1ca737171eb013e7ebe0a98087a5aa5c6ea4a499fd4dbe8be3b_1.jpg",
                "https://p16-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/a9a01b1b7e5a4ace94c0fdd9f7c45fb1~tplv-r00ih4996s-1:720:720.jpeg?x-expires=1668992400&x-signature=84BqnFgisQHFsljorNSSFMhafmg%3D",
                "https://pbs.twimg.com/media/FiBlCHtaMAACy4-?format=jpg&name=large",
                "https://img.ifunny.co/images/23d889cabc5b891c6a462b5d4e6c29ba473916f5d97fa7d4b308fd0416ba2395_3.jpg",
                "https://i.redd.it/20xda5hl361a1.jpg",
                "https://preview.redd.it/ax9164bh671a1.jpg?auto=webp&s=146b8b1c97a46dce8315f102e535250e70af8daf"
            ]
        }
    ]
}

# Create your views here.


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        total_results = []
        # t_res_template={"news_name": "","news_url": "","news_description": "","meme_url": ""}
        url = "https://bing-news-search1.p.rapidapi.com/news"

        querystring = {"setLang": 'EN', "cc": 'US',
                       "safeSearch": "Moderate", "textFormat": "Raw"}

        headers = {
            "X-BingApis-SDK": "true",
            "X-RapidAPI-Key": "4d08172c5amshe7be1524b581b3ep118814jsn1ee9225ee171",
            "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        data = response.json()
        data = data['value']
        news_names = []
        news_urls = []
        news_description = []
        for d in data:
            news_names.append(d['name'])
            news_urls.append(d['url'])
            news_description.append(d['description'])

        nlp = spacy.load("en_core_web_sm")

        s = ' '.join(news_names)
        for i in range(len(news_names)):

            doc = nlp(news_names[i])

            proper_nouns_list = extract_proper_nouns(doc)

            image_urls = []
            for i in range(len(proper_nouns_list)):
                res = re.sub(r'[^a-zA-Z]', '', str(proper_nouns_list[i]))
                if len(res) > 2:
                    q = str(proper_nouns_list[i]) + " " + " Memes"

                    q = q.replace(" ", "%20")

                    url = "https://serpapi.com/search.json?q="+q + \
                        "&tbm=isch&ijn=0&api_key=daf9ae774424cfb7f35ddf9bb59c942c04b49fa4ec6a021af3798083befd531b&tbs=qdr:d"

                    payload = {}
                    headers = {}

                    response = requests.request(
                        "GET", url, headers=headers, data=payload)

                    results = response.json()
                    i = 0
                    while i < 10:
                        image_urls.append(
                            results['images_results'][i]['original'])
                        i += 1

                    if len(image_urls) > 1:
                        t_res_template = {"news_name": news_names[i], "news_url": news_urls[i],
                                          "news_description": news_description[i], "meme_urls": image_urls}

                        total_results.append(t_res_template)

        json_object = json.dumps(total_results, indent=4)

        with open('data.json', 'w') as f:
            json.dump(json_object, f)

        return Response({'data': total_results})


def extract_proper_nouns(doc):
    pos = [tok.i for tok in doc if tok.pos_ == "PROPN"]
    consecutives = []
    current = []
    for elt in pos:
        if len(current) == 0:
            current.append(elt)
        else:
            if current[-1] == elt - 1:
                current.append(elt)
            else:
                consecutives.append(current)
                current = [elt]
    if len(current) != 0:
        consecutives.append(current)
    return [doc[consecutive[0]:consecutive[-1]+1] for consecutive in consecutives]


@api_view(['GET'])
def cached_post_collection(request):
    if request.method == 'GET':
        # f = open('data.json')
        # data = json.load(f)
        # new_data = json.dumps(data)
        return Response(return_data)


@api_view(['POST'])
def user_subscribe(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        if "@" in email_id:
            instance = Subscribers.objects.all().values_list("email_id", flat=True)
            if email_id not in instance:
                Subscribers.objects.create(email_id=email_id)
                return JsonResponse({"message": "Subscribed Successfully"})

        return JsonResponse({'data': 'failed'})


@api_view(['POST'])
def subscribe_or_not(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        if "@" in email_id:
            print(email_id)
            instance = Subscribers.objects.filter(
                email_id=email_id).values_list("email_id", flat=True)
            if len(instance) > 0:
                return JsonResponse({'data': 'true'})

    return JsonResponse({'data': 'false'})


@api_view(['GET'])
def all_subscribers(request):
    if request.method == 'GET':
        instance = Subscribers.objects.all().values_list("email_id", flat=True)
        return JsonResponse({'data': instance})
