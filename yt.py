        $API_KEY = 'AIzaSyBM2h_HOt-8J52spWsm1Gkd5LIN1C4Yyko';
        $ChannelID = 'UCiEOfLx-cmNBW4Ov-Jn_ngw';

        $channelInfo = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='.$ChannelID.'&type=video&eventType=live&key='.$API_KEY;

        $extractInfo = file_get_contents($channelInfo);
        $extractInfo = str_replace('},]',"}]",$extractInfo);
        $showInfo = json_decode($extractInfo, true);

        if($showInfo['pageInfo']['totalResults'] === 0){

        echo 'Users channel is Offline';

        }else{

        echo 'Users channel is LIVE!';

      }
