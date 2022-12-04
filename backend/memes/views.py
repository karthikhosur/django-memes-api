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
            "news_name": "Apple Makes Plans to Move Production Out of China",
            "news_url": "https://www.msn.com/en-us/money/news/apple-makes-plans-to-move-production-out-of-china/ar-AA14QCFL",
            "news_description": "In recent weeks, Apple Inc. has accelerated plans to shift some of its production outside China, long the dominant country in the supply chain that built the world’s most valuable company, say people",
            "meme_urls": [
                "https://i.imgflip.com/72z5xa.jpg",
                "https://img.ifunny.co/images/3eeb9c0a7e8cf6848f7808aca954c697c408648cee9b97eb9ee3494919e19c1b_1.jpg",
                "https://images7.memedroid.com/images/UPLOADED759/638a42fb2fda9.jpeg",
                "https://images3.memedroid.com/images/UPLOADED714/63895443f1f4a.jpeg",
                "https://img-9gag-fun.9cache.com/photo/abvzDNv_460s.jpg",
                "https://i.imgflip.com/72wqi5.jpg",
                "https://i.postimg.cc/43R58gyd/image.png",
                "https://preview.redd.it/rmewqflgrl3a1.jpg?width=640&crop=smart&auto=webp&s=eb14068bd0d73f41c2e5c1fdc88195b9f9705774",
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=1608428039614201",
                "https://img-9gag-fun.9cache.com/photo/aVbMyMK_460s.jpg"
            ]
        },
        {
            "news_name": "In Georgia runoff, GOP worries about Walker, Trump and party’s future",
            "news_url": "https://www.msn.com/en-us/news/politics/in-georgia-runoff-gop-worries-about-walker-trump-and-party-s-future/ar-AA14QvD4",
            "news_description": "   ATLANTA — Republicans have grown increasingly nervous about the final U.S. Senate election of the midterms, a runoff in Georgia that reflects larger concerns over candidate quality, infighting and",
            "meme_urls": [
                "https://i.imgflip.com/72z8vm.jpg",
                "https://i.imgflip.com/72wr3n.jpg",
                "https://i.imgflip.com/72v496.jpg",
                "https://scontent.fyka1-1.fna.fbcdn.net/v/t39.30808-6/318003205_606044551567548_1476344473701448906_n.jpg?stp=dst-jpg_s960x960&_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=TXEavw3OXy8AX9uW05d&_nc_ht=scontent.fyka1-1.fna&oh=00_AfAlwp5oAuD2wYCaDNLDAw7z2o-oJJE0xfJaVIJC5LSktQ&oe=638E757F",
                "https://pbs.twimg.com/media/Fi55HYMXEAImDsw?format=jpg&name=900x900",
                "https://preview.redd.it/c4yg8569vl3a1.png?width=640&crop=smart&auto=webp&s=8941ced6c56e91262688a354e4717e96f2c662cd",
                "https://i.redd.it/l6tuer3xnn3a1.jpg",
                "https://www.boredpanda.com/blog/wp-content/uploads/2022/12/wholesome-memes-pics-fb11.png",
                "https://preview.redd.it/3zfpmoftmn3a1.png?auto=webp&s=fdeb54c7c9fba0217e10173b1070f4bfeaf07b29",
                "https://img.ifunny.co/images/73e071fde6a31160bb4cc338a21bc343f9629554ad111def7e94f6d96941ac74_1.jpg",
                "https://i.imgflip.com/72z0c1.jpg",
                "https://i.redd.it/zll4lu9ppo3a1.jpg",
                "https://img.ifunny.co/images/3dd5b67477443bc0accfeade3e785e63c483dd517ee0dce884b2efc52bdc51d3_1.jpg",
                "https://i.ytimg.com/vi/H85rCen64sY/maxresdefault_live.jpg",
                "https://i.ytimg.com/vi/4Anw-sEwJbc/maxresdefault.jpg",
                "https://i.imgflip.com/72osjo.jpg",
                "https://pbs.twimg.com/media/Fi_eeI8XkBAY_sK?format=jpg&name=large",
                "https://img.ifunny.co/images/8177f56c9fe03f21f7f7c8fcad49f9bc9bfa35f1f58d1cd237a1f9ed2b44248e_1.jpg",
                "https://imageproxy.ifunny.co/crop:x-20,resize:640x,quality:90x75/images/5ef0985509195f0b1a19fb0df8c7aa10f9d66577d51eeffa88e505dd394f6334_1.jpg",
                "https://pbs.twimg.com/media/Fi_MOFDUUAAxgqF.jpg",
                "https://img.ifunny.co/images/167e748261005d92bea80f8e9ddd4642e77ee8b7f087cf534aa06a56bd332095_1.jpg",
                "https://i.imgflip.com/72z8vm.jpg",
                "https://img.ifunny.co/images/d35fa00e8e6ac76aca7b3da92c4d7dcb9b4bcac21acde3e54bba410405715dd6_1.jpg",
                "https://i.imgflip.com/72z0c1.jpg",
                "https://i.kym-cdn.com/photos/images/original/002/489/405/c96.png",
                "https://img.ifunny.co/images/937c39b3492b61afa50045f5eecfaab23eed9a529b8cca6f2bd91c03e21407a5_1.jpg",
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=10159590347104833",
                "https://i.imgflip.com/72ye26.jpg",
                "https://img.ifunny.co/images/ad65588ee10a27fb447fc50bd13a1ea1ab3f2c33440cea0c737196313506435a_3.jpg",
                "https://p16-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/8fc369845bf2428cbbbae33880f031d7~tplv-r00ih4996s-1:720:720.jpeg?x-expires=1670043600&x-signature=%2BrbNncnpJHBOzHCI5zkTULawIsM%3D",
                "https://i.imgflip.com/72ywba.jpg",
                "https://i.imgflip.com/72xil8.jpg",
                "https://i.imgflip.com/72vaho.jpg",
                "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oYkPNAretJAUeDQjMh8bBBQ8ArPjYSISRhn8Ex~tplv-f5insbecw7-1:720:720.jpeg?x-expires=1670068800&x-signature=LmNs4mXwByvKAh9jTREd0jj%2BoRU%3D",
                "https://www.tiktok.com/api/img/?itemId=7172654162541399338&location=0&aid=1988",
                "https://i.imgflip.com/6x2gp8.jpg",
                "https://i.imgflip.com/72w1vd.jpg",
                "https://pbs.twimg.com/media/Fi_qh8UWAA8F4SV.jpg",
                "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=2984533913456173926",
                "https://pbs.twimg.com/media/Fi_eeI8XkBAY_sK.jpg"
            ]
        },
        {
            "news_name": "Biden signs bill to block U.S. railroad strike",
            "news_url": "https://www.msn.com/en-us/news/us/biden-signs-bill-to-block-us-railroad-strike/ar-AA14P4de",
            "news_description": "By David Shepardson and Nandita BoseWASHINGTON (Reuters) -President Joe Biden signed legislation Friday to block a national U.S. railroad strike that could have devastated the American economy.The U",
            "meme_urls": [
                "https://i.imgflip.com/72z5px.jpg",
                "https://i.imgflip.com/72ye26.jpg",
                "https://i.imgflip.com/72xzrh.jpg",
                "https://i.imgflip.com/72zauw.jpg",
                "https://www.tiktok.com/api/img/?itemId=7169805284779593003&location=0&aid=1988",
                "https://i.imgflip.com/72zr5d.jpg",
                "https://i.imgflip.com/72z8wg.jpg",
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=5753488648030828",
                "https://i.imgflip.com/6fzbrf.jpg",
                "https://images3.memedroid.com/images/UPLOADED30/638a64f013aa2.jpeg"
            ]
        },
        {
            "news_name": "Supreme Court to debate whether businesses may decline to provide services to same-sex weddings",
            "news_url": "https://www.msn.com/en-us/news/us/supreme-court-to-debate-whether-businesses-may-decline-to-provide-services-to-same-sex-weddings/ar-AA14R27F",
            "news_description": "             WASHINGTON – A spontaneous celebration erupted outside the Supreme Court in 2015 when a slim majority of the justices legalized same-sex marriage across the nation. Gay pride flags",
            "meme_urls": [
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=606543561517647",
                "https://images7.memedroid.com/images/UPLOADED656/638ade94043d4.jpeg",
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=711836703830824",
                "https://preview.redd.it/omg-they-actually-made-a-funny-meme-v0-7qhu6bk1bl3a1.jpg?auto=webp&s=737a7282934d887d1e1af19e588ab4f29ba53483",
                "https://i.imgflip.com/6x2gp8.jpg",
                "https://img.ifunny.co/images/ddf99d3d59dbc2b5e10492d1bc3fac5beb7267a702c62ab5af516c0b13cecbcf_1.jpg",
                "https://preview.redd.it/ld3pjik16j3a1.jpg?auto=webp&s=045e4f4a08a42876f318bd1e626c63bd356ee96b",
                "https://i.imgflip.com/72z5xa.jpg",
                "https://static.wikia.nocookie.net/2f9366c9-118b-4b1c-98ae-7b7caba86e94/scale-to-width/755",
                "https://i.ytimg.com/vi/A9AWwEk_XjE/maxresdefault.jpg"
            ]
        },
        {
            "news_name": "Suspect arrested for allegedly shooting teen campaigning for Raphael Warnock",
            "news_url": "https://www.msn.com/en-us/news/crime/suspect-arrested-for-allegedly-shooting-teen-campaigning-for-raphael-warnock/ar-AA14Qkw4",
            "news_description": "  A Georgia man was arrested for allegedly firing a gun through his front door at a teenager volunteering for Sen. Raphael Warnock's campaign, striking the boy in the leg, police said.   The incident",
            "meme_urls": [
                "https://external-preview.redd.it/court-justice-system-in-bedfordshire-uk-is-a-joke-v0-Pg88hT-r_NGcKYRgI1rdakLOl6fNIc5SOfcEgyFOT5Q.png?format=pjpg&auto=webp&s=ef3e5ee91de6f682bd06fea94da3969c039b3d2d",
                "https://pbs.twimg.com/media/Fi_r4eMX0AEKSUS.jpg",
                "https://img.ifunny.co/images/5905742231dce377a1e1dd02b364a7ade6f7c65aa1f0614bd3507fddc664f47b_3.jpg",
                "https://i.imgflip.com/72x8y2.jpg",
                "https://pbs.twimg.com/media/Fi_biOMVEAAwWAS.jpg",
                "https://images3.memedroid.com/images/UPLOADED531/638a1395a52f0.jpeg",
                "https://i.redd.it/k4wzyi1emk3a1.png",
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=6443398002344172",
                "https://img.ifunny.co/images/7e80903955ba1b1b2477806c3107e9ca75ba8027b3b760c122c86c81a3e4e76b_1.jpg",
                "https://heavy.com/wp-content/uploads/2022/12/patrick-xavier-clark.jpg?quality=65&#038;strip=all&#038;w=780",
                "https://img.ifunny.co/images/937c39b3492b61afa50045f5eecfaab23eed9a529b8cca6f2bd91c03e21407a5_1.jpg",
                "https://img.ifunny.co/images/9d524335265d4a100ed41ab31357d8fcf83d86acf1d98bbd5d274eabde358c4a_1.jpg",
                "https://img.ifunny.co/images/73e071fde6a31160bb4cc338a21bc343f9629554ad111def7e94f6d96941ac74_1.jpg",
                "https://img.ifunny.co/images/f202e92758fb8fd2214929d73dc5110dbf23438306c2a9d2611b12f099118b5c_3.jpg",
                "https://s.abcnews.com/images/Politics/WireAP_a9dcb1ee147642e19c224b5381a8fce2_16x9_1600.jpg",
                "https://static.politico.com/c0/02/5b2eef6447b29ff28ff11335bde7/election-2022-senate-georgia-46908.jpg",
                "https://i.ytimg.com/vi/rDQMYHgGBK0/maxresdefault.jpg",
                "https://static01.nyt.com/images/2022/12/02/multimedia/02xp-savannah-1-9fa2/02xp-savannah-1-9fa2-thumbLarge.jpg?quality=75&auto=webp&disable=upscale",
                "https://wfxl.com/resources/media2/16x9/full/1015/center/80/d63bee4a-b9e6-4fe2-8cf7-35736f7f957f-large16x9_AP223337650305111.jpg",
                "https://storage.googleapis.com/afs-prod/media/eb2a1f98234f49a69e69636c2444f728/3000.jpeg"
            ]
        },
        {
            "news_name": "Russia rejects $60-a-barrel cap on its oil, warns of cutoffs",
            "news_url": "https://www.msn.com/en-us/news/world/russia-rejects-60-a-barrel-cap-on-its-oil-warns-of-cutoffs/ar-AA14RDAt",
            "news_description": "KYIV, Ukraine (AP) — Russian authorities rejected a price cap on the country's oil set by Ukraine’s Western supporters and threatened Saturday to stop supplying the nations that endorsed it.",
            "meme_urls": [
                "https://i.imgflip.com/72rusj.jpg",
                "https://preview.redd.it/there-lived-a-certain-man-in-russia-long-ago-v0-bnw6g1nzhl3a1.gif?width=640&crop=smart&format=png8&s=b6042210c9241067be3fec13e28626e83a3dd5c1",
                "https://img-9gag-fun.9cache.com/photo/awZQjRr_460s.jpg",
                "https://i.ytimg.com/vi/2kUUQ50Dnf4/maxresdefault.jpg",
                "https://i.imgflip.com/72ygre.jpg",
                "https://preview.redd.it/well-then-v0-sibt5clq9j3a1.png?auto=webp&s=bb2af974d558d8616c8169809ff57fe7c800bfc9",
                "https://thesocialtalks.com/ezoimgfmt/i.ibb.co/Hd7k6LQ/memes2.jpg?ezimgfmt=rs:221x221/rscb4/ngcb4/notWebP",
                "https://preview.redd.it/erdogan-about-to-shoot-down-some-more-russian-jets-v0-b14tgz2ekk3a1.jpg?auto=webp&s=eae983262eb1ce0324d8b05587ae67de36b0f8ff",
                "https://preview.redd.it/india-is-gonna-be-suffering-v0-u4nf47yckm3a1.jpg?width=640&crop=smart&auto=webp&s=8862fd5d766cb51301cf694436ceb79cba6b5509",
                "https://i.imgflip.com/72z3qc.jpg"
            ]
        },
        {
            "news_name": "Prosecutor turns focus on Donald Trump as company's tax fraud trial ends",
            "news_url": "https://www.msn.com/en-us/news/us/prosecutor-turns-focus-on-donald-trump-as-companys-tax-fraud-trial-ends/ar-AA14Q9Si",
            "news_description": "By Karen Freifeld and Luc CohenNEW YORK (Reuters) -   Donald Trump's namesake real estate company engaged in tax fraud and the former U.S. president knew it was going on, a prosecutor said in closing",
            "meme_urls": [
                "https://i.imgflip.com/72ywba.jpg",
                "https://i.imgflip.com/72zlcr.jpg",
                "https://www.tiktok.com/api/img/?itemId=7172654162541399338&location=0&aid=1988",
                "https://i.imgflip.com/72xil8.jpg",
                "https://i.imgflip.com/72y54g.jpg",
                "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oYkPNAretJAUeDQjMh8bBBQ8ArPjYSISRhn8Ex~tplv-f5insbecw7-1:720:720.jpeg?x-expires=1670068800&x-signature=LmNs4mXwByvKAh9jTREd0jj%2BoRU%3D",
                "https://i.imgflip.com/72vaho.jpg",
                "https://pbs.twimg.com/media/Fi_0dU8WAA0YlEK?format=jpg&name=large",
                "https://lookaside.instagram.com/seo/google_widget/crawler/?media_id=2984533913456173926",
                "https://pbs.twimg.com/media/Fi-OoGfXwAEh5Wf.jpg"
            ]
        },
        {
            "news_name": "Arrest made in killing of Migos rapper Takeoff",
            "news_url": "https://www.msn.com/en-us/news/us/arrest-made-in-killing-of-migos-rapper-takeoff/ar-AA14QiFl",
            "news_description": "  A suspect has been arrested and charged with murder in the fatal shooting of Migos rapper Takeoff, Houston police said Friday.MORE: Fans pay tribute to slain rapper Takeoff in Atlanta celebration",
            "meme_urls": [
                "https://www.tiktok.com/api/img/?itemId=7161025687728475397&location=0&aid=1988",
                "https://img.ifunny.co/images/b11202ab6fc611d9579bc03206b7c6bf7338b0e0fed771785a903275e191b6c5_1.jpg",
                "https://cdn.kapwing.com/collections/image_63872f83c0af4c00116f2b55_292206.jpeg",
                "https://img.ifunny.co/images/af6f66631199b15fa501e64b2b6e8121f03eb403a886c2ff05a131e16d355948_1.jpg",
                "https://img.ifunny.co/images/46f6b70e505bf5384aa322de657e60098af3f3f1e84bdaebaf2aef64e3a6d961_1.jpg",
                "https://cdn.kapwing.com/collections/final_638a6cd7dde63300a4f1fb02_758923.gif",
                "https://p16-sign-va.tiktokcdn.com/obj/tos-maliva-p-0068/330c7024ffbc493c98fef614560063e0_1669997575?x-expires=1670043600&x-signature=HKqKxfJ%2Bl9J5WvHn1I75X8jSpGU%3D",
                "https://pbs.twimg.com/ext_tw_video_thumb/1598875189265039360/pu/img/eJPxLh7ji0L1OnhH.jpg",
                "https://img.ifunny.co/images/f6546af7da633103100a659f63804a3adabefaea08f7c785839d4d4f0567dbcb_1.jpg",
                "https://img.ifunny.co/images/a997475a4a1df8e4cabf76e21e7d4339eb22545d5f5e1b68018dcdf95b1fe1eb_1.jpg",
                "https://www.tiktok.com/api/img/?itemId=7161025687728475397&location=0&aid=1988",
                "https://pbs.twimg.com/ext_tw_video_thumb/1598773708121903111/pu/img/lydbEqQvxI48EEnu.jpg",
                "https://pbs.twimg.com/media/FjAJAoxXEAwARit.jpg",
                "https://pbs.twimg.com/media/FjAO2OYWYAA0yis.jpg",
                "https://p19-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/f12e6b30da9a4bc39b965e156c7fed71~tplv-r00ih4996s-1:720:720.jpeg?x-expires=1670061600&x-signature=WwacmRbVF5mzfgSWvsCP%2FHnJ8ZA%3D",
                "https://pbs.twimg.com/media/FjAbvi1X0AA7OCD.jpg",
                "https://www.wivb.com/wp-content/uploads/sites/97/2022/12/6eef98f1f8314aca92b97df281852737.jpg?w=900",
                "https://cdn.vox-cdn.com/thumbor/L_M7t60rEca4bcWMG4_Wc0yZ4dA=/240x0:1680x1080/340x255/cdn.vox-cdn.com/uploads/chorus_image/image/71700490/DIALLO.0.jpeg",
                "https://static.toiimg.com/thumb/msid-95953703,width-1070,height-580,overlay-toi_sw,pt-32,y_pad-40,resizemode-75,imgsize-31624/95953703.jpg",
                "https://pbs.twimg.com/media/FjACsJeXEBwo9oV?format=jpg&name=large"
            ]
        },
        {
            "news_name": "USA vs. Netherlands World Cup live updates: Americans trail after Memphis Depay's early goal",
            "news_url": "https://www.msn.com/en-us/sports/fifa-world-cup/usa-vs-netherlands-world-cup-live-updates-americans-trail-after-memphis-depays-early-goal/ar-AA14RvoR",
            "news_description": "             The U.S. men's national team, which included only one player who had any World Cup experience coming into this tournament, faces the Netherlands on Saturday at 10 a.m. ET. While many",
            "meme_urls": [
                "https://i.imgflip.com/72wcnl.jpg",
                "https://shutupandtakemymoney.com/wp-content/uploads/2020/05/i-bought-four-pounds-worth-of-bread-uk-vs-usa-meme.jpg",
                "https://preview.redd.it/this-is-the-american-way-v0-uhgphxaezi3a1.png?width=640&crop=smart&auto=webp&s=45f23ae3700a7578e5f93ee86d41b6ff63626740",
                "https://img-9gag-fun.9cache.com/photo/awZQjRr_460s.jpg",
                "https://i.kym-cdn.com/photos/images/facebook/002/488/891/683.jpg",
                "https://cdn.memes.com/up/34528681649863107/i/1670032755141.jpg",
                "https://i.imgflip.com/37lbvm.jpg",
                "https://img.ifunny.co/images/0e674e7e2460d745222f8fea3d153c87e776606625b0b6b053adce2f8f8fdd46_1.jpg",
                "https://images3.memedroid.com/images/UPLOADED514/638a48e91412b.jpeg",
                "https://p16-sign.tiktokcdn-us.com/obj/tos-useast5-p-0068-tx/32bda71fcdb242c5b54cb81c664b1629?x-expires=1670050800&x-signature=yqTZyrVrf1aAgOFnnokXJIF9U44%3D",
                "https://img.ifunny.co/images/d49b2d5ad2da3931f014de3646d94d509fefe4728040c7482fa4ed781e21a5fd_1.jpg",
                "https://nypost.com/wp-content/uploads/sites/2/2022/12/usa-netherlands-world-cup-soccer-comp.jpg?quality=75&strip=all",
                "https://i.guim.co.uk/img/media/56cf9190fce4a7cea35f80a57295dd48ac79704b/0_0_5000_3000/master/5000.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=7416543808a4b9e3722e3590a6705e74",
                "https://nypost.com/wp-content/uploads/sites/2/2022/12/world-soccer4-1.jpg?quality=75&strip=all&w=744",
                "https://wjla.com/resources/media/74c1b26c-1c6f-4d42-9bbb-d5e643ef4e23-medium16x9_AP22333718173620.jpg?1670013963222",
                "https://s01.sgp1.cdn.digitaloceanspaces.com/article/183795-pcmqvpqnql-1670043650.jpg",
                "https://cdn.resfu.com/scripts/tmp_images/afp_en_4835abdb161b3b9d4500652eff9c1cc42bcbae08.jpg?size=1000x&lossy=1",
                "https://d3nfwcxd527z59.cloudfront.net/content/uploads/2022/12/02152618/Kevin-De-Bruyne.jpg",
                "https://phantom-marca.unidadeditorial.es/7d5db2b78429ae9efdb26a79c3d8975c/crop/0x0/2044x1363/resize/1320/f/jpg/assets/multimedia/imagenes/2022/12/03/16700728929105.jpg",
                "https://static.india.com/wp-content/uploads/2022/12/Collage-Maker-03-Dec-2022-06.29-PM.jpg?impolicy=Medium_Resize&w=1200&h=800",
                "https://pbs.twimg.com/media/FjEDPIbWIAE-kcZ?format=jpg&name=large",
                "https://pbs.twimg.com/media/FjAF_d9XEBYydEi.jpg",
                "https://pbs.twimg.com/media/Fi_WI_oXkBIyeca.jpg",
                "https://pbs.twimg.com/media/Fi_SVz6XwAEoSK_.jpg",
                "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=539664294842556",
                "https://cdn1-production-images-kly.akamaized.net/FQG0N7zCCaGv-ghHUGfgnInoMIQ=/1200x1200/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/thumbnails/4248488/original/013269100_1670053147-klasemen-grup-g-h_-brasil-dan-swiss-ke-16-besar-diikuti-portugal-dan-korsel-_-060089.jpg",
                "https://i.dailymail.co.uk/1s/2022/12/03/15/65204605-0-image-a-33_1670080557264.jpg",
                "https://laopinion.com/wp-content/uploads/sites/3/2022/12/Alemania-quedo-afuera-en-la-primera-ronda-de-Qatar-2022..jpg?quality=60&strip=all&w=300",
                "https://pbs.twimg.com/media/Fi_RnRMWAAIaSZf.jpg",
                "https://nypost.com/wp-content/uploads/sites/2/2022/12/usa-netherlands-world-cup-soccer-comp.jpg?quality=75&strip=all&w=1024"
            ]
        },
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

            image_urls = get_image_urls(proper_nouns_list)
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


def get_image_urls(proper_nouns_list):
    image_urls = []
    for i in range(len(proper_nouns_list)):
        res = re.sub(r'[^a-zA-Z]', '', str(proper_nouns_list[i]))
        if len(res) > 2:
            q = str(proper_nouns_list[i]) + " " + " Memes"

            q = q.replace(" ", "%20")

            url = "https://serpapi.com/search.json?q="+q + \
                "&tbm=isch&ijn=0&api_key=ef7a056dd2c29f170be3ad8780b694559f49d7abced95a4d62bec1e5bcc9b52f&tbs=qdr:d"

            payload = {}
            headers = {}

            response = requests.request(
                "GET", url, headers=headers, data=payload)

            results = response.json()
            i = 0
            while i < 10:
                image_urls.append(results['images_results'][i]['original'])
                i += 1
    return image_urls


@api_view(['GET'])
def cached_post_collection(request):
    if request.method == 'GET':
        return Response(return_data)


@api_view(['POST'])
def user_subscribe(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        if "@" in email_id:
            instance = Subscribers.objects.all().values_list("email_id", flat=True)
            if email_id not in instance:
                Subscribers.objects.create(email_id=email_id)
                print("Subscribed")
                send_simple_message(email_id)
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
        return Response({'data': instance})


def send_simple_message(email_id):
    print("sending")
    return requests.post(
        "https://api.mailgun.net/v3/sandbox06ea921aa2234525b0590aa0fdd423ed.mailgun.org/messages",
        auth=("api", "96b2666359c7d2a91edf06c7b5b5eb2c-680bcd74-25527948"),
        data={"from": "Excited User <karthikhosur15@gmail.com>",
              "to": [email_id],
              "subject": "Thank You for Subscribing ",
              "text": " You have agreed to recive daily newsletters. Thank You for joining us !"})
