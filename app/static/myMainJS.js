// Scroll
document.body.scrollTop = document.body.scrollHeight;


// PRELOAD

function loadData() {
  return new Promise((resolve, reject) => {
    setTimeout(resolve, 2000);
  })
}

loadData()
  .then(() => {
    let preloaderEl = document.getElementById('wrapper');
    preloaderEl.classList.add('hidden');
    preloaderEl.classList.remove('visible');
  });


// TITLE anim script

$('.txt').html(function(i, html) {
    var chars = $.trim(html).split("");
    return '<span>' + chars.join('</span><span>') + '</span>';
});

// /*----------------------------------------------------------------------------*/
//                                   BUTTON                                    
// /*----------------------------------------------------------------------------*/

var animateButton = function(e) {

  e.preventDefault;
  //reset animation
  e.target.classList.remove('animate');
  
  e.target.classList.add('animate');
  setTimeout(function(){
    e.target.classList.remove('animate');
  },700);
};

var bubblyButtons = document.getElementsByClassName("bubbly-button");

for (var i = 0; i < bubblyButtons.length; i++) {
  bubblyButtons[i].addEventListener('click', animateButton, false);
}

// /*----------------------------------------------------------------------------*/
//                                   AUDIO                                    
// /*----------------------------------------------------------------------------*/

var song = new Audio();
var muted = false;
var vol = 1;
var index_song = -1;
song.type = 'audio/mpeg';
var e_dict = {key:'Enter'};
myMusic(e_dict);

function play_choose(url, index) {
    

    if (document.getElementById('but_{0}'.f(index)).id == 'but_{0}'.f(index_song)) {
        document.getElementById('but_{0}'.f(index_song)).innerHTML = "<i class='icon-play'</i>";
        document.getElementById('playpause').innerHTML = "<i class='icon-play'</i>";
        playpause()

    } else {
        try {
                    if (document.getElementById('but_{0}'.f(index)).id != 'but_{0}'.f(index_song)) {
              document.getElementById('but_{0}'.f(index_song)).className = 'but_'
              document.getElementById('but_{0}'.f(index_song)).innerHTML = "<i class='icon-play'</i>";
            }
        } catch {
            console.log()
        }


        $('#text_song').text(document.getElementById('text_song_{0}'.f(index)).textContent)

        document.getElementById('but_{0}'.f(index)).className = 'but'
        document.getElementsByClassName('but')[0].innerHTML = "<i class='icon-pause'</i>";
        document.getElementById('playpause').innerHTML = "<i class='icon-pause'</i>";

        song.src = url;
        index_song = parseInt(index);
        $('.time_song').text('{0}:{1}'.f(parseInt(parseInt(song.duration)/60), parseInt(song.duration)%60));

        song.play()
    }

};


setInterval(function () {

    if (song.ended) {
        if ($('#row_playlist_{0}'.f(index_song+1)).attr('url') != null) {
            document.getElementsByClassName('but')[0].innerHTML = "<i class='icon-play'</i>";
            document.getElementById('but_{0}'.f(index_song)).className = 'but_'
            index_song += 1;
            document.getElementById('but_{0}'.f(index_song)).className = 'but'
            song.src = $('#row_playlist_{0}'.f(index_song)).attr('url');
            document.getElementsByClassName('but')[0].innerHTML = "<i class='icon-pause'</i>";
            document.getElementById('playpause').innerHTML = "<i class='icon-pause'</i>";
            song.play();
            $('#text_song').text(document.getElementById('text_song_{0}'.f(index_song)).textContent)
        } else {
            song.src = $('#row_playlist_{0}'.f(index_song)).attr('url');
            $('.time_song').text('{0}:{1}'.f(parseInt(parseInt(song.duration)/60), parseInt(song.duration)%60));
            document.getElementsByClassName('but')[0].innerHTML = "<i class='icon-play'</i>"
            document.getElementsByClassName('but').innerHTML = "<i class='icon-play'</i>";
            stop();
        }
    }
    if (parseInt(parseInt(song.duration)/60) < 1) {
        $('.time_song').text('{0}:{1}'.f(0, (parseInt(song.duration) - parseInt(song.currentTime))%60));
    } else {
        $('.time_song').text('{0}:{1}'.f(parseInt((parseInt(song.duration) - parseInt(song.currentTime))/60), (parseInt(song.duration) - parseInt(song.currentTime))%60));
    }
    
}, 1000);


function skip(time) {
    if (time == 'back') {
        song.currentTime = (song.currentTime - 5);
        
    } else if (time == 'fwd') {
        song.currentTime = (song.currentTime + 5);
    }
};

function playpause() {
    if (!song.paused) {
        try{
            document.getElementsByClassName('but')[0].innerHTML = "<i class='icon-play'</i>";
        } catch {
            console.log();
        }
        
        document.getElementById('playpause').innerHTML = "<i class='icon-play'</i>"
        song.pause();
    } else {
        try {
            document.getElementsByClassName('but')[0].innerHTML = "<i class='icon-pause'</i>";
        } catch {
            console.log();
        }
        document.getElementById('playpause').innerHTML = "<i class='icon-pause'</i>";
        
        song.play();
    }
};

function stop() {
    song.pause();
    song.currentTime = 0;
    document.getElementById('seek').value = 0;
    $('.time_song').text('{0}:{1}'.f(parseInt(parseInt(song.duration)/60), parseInt(song.duration)%60));
    document.getElementById('playpause').innerHTML = "<i class='icon-play'</i>";
    try {
        document.getElementsByClassName('but')[0].innerHTML = "<i class='icon-play'</i>";
    } catch {
        console.log()
    }
    
}

function setPos(pos) {
    song.currentTime = pos;
    
}

function mute() {
    if (muted) {
        if (vol!=0) {
            song.volume = vol;
            muted = false;
            document.getElementById('mute').innerHTML = '<td class="chars">🔊</td>';
        }
    } else {
    song.volume = 0;
    muted = true;
    document.getElementById('mute').innerHTML = '<td class="chars">🔇</td>';
    }
}

function setVolume(volume) {
    song.volume = volume;
    vol = volume;
    
    if (vol==0){
        song.volume = 0;
        muted = true;
        document.getElementById('mute').innerHTML = '<td class="chars">🔇</td>';
    } else {
        song.volume = vol;
        muted = false;
        document.getElementById('mute').innerHTML = '<td class="chars">🔊</td>';
    }
}
song.addEventListener('timeupdate',function() {
    curtime = parseInt(song.currentTime,10);
    document.getElementById('seek').max = song.duration;
    document.getElementById('seek').value = curtime;
})

var url_text = ''

function pasteUrl(url) {
    url_text = url
    try {
        clearInterval(intervalTime);
        // document.getElementById('input_url').value = url;
        activate_Timer();
    } catch (e) {
        console.log(e)
    }

};

function pasteMusic(SRC){
  $('#audio').html('<audio autoplay controls="controls" name="media"><source src="{0}" type="audio/mpeg"></audio>'.f(SRC));
};

// var startPars = setInterval(start, 1000)
// function start(){
//     $.ajax({
//         url: "/",
//         type: "get"
//     });
// };

String.prototype.format = String.prototype.f = function() {
        var s = this,
            i = arguments.length;

        while (i--) {
            s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
        }
        return s;
    };

var watchButton = document.getElementById("watch_video");
watchButton.onclick = myWatch;

// var musicButton = document.getElementById("get_music");
// musicButton.onclick = myMusic;

function myMusic(e) {
    console.log(e.key)
    index_song = -1
    if (e.key == 'Enter' || e.type == 'click') {
        try{
            e.preventDefault()
        } catch {
            console.log()
        }
        var mySearch = $(".music").val();
        $.ajax({
                url: "/music",
                type: "get",
                data: {jsdata: mySearch},
                dataType: "json",
                success: function(response) {
                  var music_dict = JSON.parse(response.music)
                  var textTagMusicList = ''
                      for (var _ in music_dict)
                      {
                        textTagMusicList = textTagMusicList +'<div id="row_playlist"><div id="row_playlist_{3}" url={2}><div id="playlist_content"><button class="but_" id="but_{3}" onclick="play_choose({2}, {3})"><td class="chars_playlist"><i class="icon-play"></i></td></button></div><div id="text_song_{3}">{0} - {1}</div></div></div>'.f(music_dict[_][0], music_dict[_][1], "'{0}'".f(music_dict[_][2]), _);
                      }
                  $('.playlist').html(textTagMusicList);
                    }
            });
        }

};

function myWatch() {

    var videoWatch = $(".videotext").val();
    
  $('#Video').html('<iframe frameborder="1" src="{0}" width="900" height="505" frameborder="0" allow="autoplay; fullscreen" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>'.f(videoWatch));

}

// function loopConnect(){
//   var myVar = setInterval(connect, 1000);
// }

var intervalTime

function activate_Timer() {
    intervalTime = setInterval(function(){
            $.ajax({
                url: "/parsing",
                type: "get",
                data: {jsdata: url_text},
                dataType: "json",
                success: function(response) {
                  var dict = JSON.parse(response.stats);
                  var graf = JSON.parse(response["stats_graf"]);
                  var textTagGameList = ''
                  for (var gaMe in dict['game_list']) {
                      try {                  
                            textTagGameList = textTagGameList + '<button class="up" onclick="pasteUrl({1})">{0}</button><br>'.f(gaMe, "'{0}'".f(dict['game_list'][gaMe]));
                              // document.getElementByClassName('').innerHTML
                          } catch (e) {
                            console.log(e);
                          };
                      };
                  $('.buttons').html(textTagGameList);
                  // $("#stats").html(response.stats);
                  console.log(response['stats_graf']);
                  $("title").text('{0}   {1}'.f(dict["timer"], dict["game"]));

                <!--Спарсеные параметры-->
                    // $("#timer").text(dict["timer"]);

                    var timer_sec = parseInt(dict["timer"].split(':')[1]);
                    var timer_min = parseInt(dict["timer"].split(':')[0]);
                    // console.log(parseFloat(timer_min/100), parseFloat(timer_sec/1000))

                    $('meter[id="meter_math"]').val(timer_sec);
                    // $("#name_match").text(dict["match"]);
                    // $('div[id="__tag__"]').html(dict["_tag_"]);

                <!--Переменные для времени-->
                    
                    var for_input = [
                    ['input[name="fouls"]', "#fouls_time", dict["фолы"], "#fouls_math", "#fouls_sub", "fouls_gif", "фолы"],
                    ['input[name="SOT"]', "#SOT_time", dict["удары в створ"], "#SOT_math", "#SOT_sub", "SOT_gif", "удары в створ"],
                    ['input[name="auts"]', "#auts_time", dict["вброс аутов"], "#auts_math", "#auts_sub", "auts_gif", "вброс аутов"],
                    ['input[name="SAT"]', "#SAT_time", dict["удары от ворот"], "#SAT_math", "#SAT_sub", "SAT_gif", "удары от ворот"],
                    ['input[name="corner"]', "#corner_time", dict["угловые"], "#corner_math", "#corner_sub", "corner_gif", "угловые"],
                    ['input[name="ycard"]', "#ycard_time", dict["жёлтые карты"], "#ycard_math", "#ycard_sub", "ycard_gif", "желтые карты"],
                    ['input[name="ofsaid"]', "#ofsaid_time", dict["офсайды"], "#ofsaid_math", "#ofsaid_sub", "ofsaid_gif", "офсайды"]
                                    ]

                    for (var _ in for_input)
                    {

                        var min = parseInt(45/$(for_input[_][0]).val());
                        var sec = parseInt((45/$(for_input[_][0]).val())%1*60);
                        $(for_input[_][1]).text(min + ':' + sec);
                        var math_min = timer_min + parseInt(min*parseInt(for_input[_][2])) + parseInt((sec*parseInt(for_input[_][2])+timer_sec)/60);
                        var math_sec = parseInt(sec*parseInt(for_input[_][2])+timer_sec)%60;
                        
                        $(for_input[_][3]).html("<strong>{0}:{1} | {2}</strong><sup> ({5}:{6}) </sup><hr><br><strong>{3}</strong><sup> ({4}) </sup>".f(math_min, math_sec, for_input[_][2], dict[for_input[_][6]+" Total"], dict[for_input[_][6]+" БМ"], dict[for_input[_][6]+" K1"], dict[for_input[_][6]+" K2"]));
                        // $(for_input[_][4]).text(for_input[_][2]);

                        
                        if (isNaN(math_min) == false)
                        {
                            if (dict['TIME'] == 1)
                            {   
                                if (math_min > 47)
                                {
                                    document.getElementById(for_input[_][5]).className = 'YES_gif';
                                }else document.getElementById(for_input[_][5]).className = 'NO_gif';
                            }
                            
                            if (dict['TIME'] == 0)
                            {
                                if (math_min > 92)
                                {
                                    document.getElementById(for_input[_][5]).className = 'YES_gif';
                                }else document.getElementById(for_input[_][5]).className = 'NO_gif';
                            }
                        }
                    }


                            var _width = 950;
                            var _height = 100;
                            var _step = 10;
                            var _list = [
                                            [document.getElementById("Canvas_fouls"),
                                            document.getElementById("Canvas_fouls").getContext('2d'),
                                            "фолы - "],

                                            [document.getElementById("Canvas_SOT"),
                                            document.getElementById("Canvas_SOT").getContext('2d'),
                                            "удары в створ - "],

                                            [document.getElementById("Canvas_auts"),
                                            document.getElementById("Canvas_auts").getContext('2d'),
                                            "вброс аутов - "],

                                            [document.getElementById("Canvas_SAT"),
                                            document.getElementById("Canvas_SAT").getContext('2d'),
                                            "удары от ворот - "],

                                            [document.getElementById("Canvas_corner"),
                                            document.getElementById("Canvas_corner").getContext('2d'),
                                            "угловые - "],

                                            [document.getElementById("Canvas_ycard"),
                                            document.getElementById("Canvas_ycard").getContext('2d'),
                                            "жёлтые карты - "],

                                            [document.getElementById("Canvas_ofsaid"),
                                            document.getElementById("Canvas_ofsaid").getContext('2d'),
                                            "офсайды - "]
                                        ]

                            var colors = ["aqua", "black", "blue", "fuchsia", "green", "cyan", "lime", "maroon",
                                        "navy", "olive", "purple", "red", "silver", "teal", "yellow", "azure",
                                        "gold", "bisque", "pink", "orange"];
                            // var numColors = colors.length;
                            // var colorIndex = Math.random() * (numColors - 1);
                            //     colorIndex = Math.round(colorIndex);
                            // var color = colors[colorIndex];

                            for (var i in _list)
                            {   

                                _list[i][0].width = _width;
                                _list[i][0].height = _height;

                                _list[i][1].fillStyle = "black";
                                _list[i][1].lineWidth = 2;
                                _list[i][1].beginPath();
                                _list[i][1].moveTo(10, parseInt(_height/2)); // Начало линии
                                _list[i][1].lineTo(910, parseInt(_height/2)); // Конец линии 
                                _list[i][1].stroke();
                                _list[i][1].font = "7pt lucida console";
                                for (var j = 0; j < 91; )
                                    {  
                                        _list[i][1].textAlign = "center";
                                        _list[i][1].fillText(parseInt(j), _step*parseInt(j) + 10, parseInt(_height/2) + 20);
                                        j += 5;
                                        if (j > 90) break
                                        _list[i][1].beginPath();
                                        _list[i][1].moveTo(_step*parseInt(j) + 10, parseInt(_height/2)-8);
                                        _list[i][1].lineTo(_step*parseInt(j) + 10, parseInt(_height/2)+8); 
                                        _list[i][1].stroke();
                                    }

                                for (var k = 0; k < 91; k++)
                                    {  
                                        if (k%5 == 0) continue
                                        _list[i][1].strokeStyle = 'black';
                                        _list[i][1].lineWidth = 1;
                                        _list[i][1].beginPath();
                                        _list[i][1].moveTo(_step*parseInt(k) + 10, parseInt(_height/2)-5);
                                        _list[i][1].lineTo(_step*parseInt(k) + 10, parseInt(_height/2)+5); 
                                        _list[i][1].stroke();
                                    }
                                for (var num = 0; num < 91; num++)
                                {
                                    try
                                    {
                                        N = graf[_list[i][2]+num+' минута'][3];
                                        _list[i][1].font = "7pt segoe print";
                                        _list[i][1].fillStyle = "black";
                                        _list[i][1].textAlign = "center";
                                        _list[i][1].fillText(N, _step*parseInt(num)+5, parseInt(_height/2)-23-parseInt(N)*5);
                                        // diagram
                                        _list[i][1].strokeStyle = 'aqua';
                                        _list[i][1].lineWidth = 3;
                                        _list[i][1].beginPath();
                                        _list[i][1].moveTo(_step*parseInt(num) + 5, parseInt(_height/2));
                                        _list[i][1].lineTo(_step*parseInt(num) + 5, parseInt(_height/2)-20-parseInt(N)*5);
                                        _list[i][1].stroke();

                                        sub_N = graf[_list[i][2]+(num-1)+' минута'][3];
                                        // line for diagram
                                        _list[i][1].strokeStyle = 'blue';
                                        _list[i][1].lineWidth = 1;
                                        _list[i][1].beginPath();
                                        _list[i][1].moveTo(_step*parseInt(num-1) + 5, parseInt(_height/2)-20-parseInt(sub_N)*5);
                                        _list[i][1].lineTo(_step*parseInt(num) + 5, parseInt(_height/2)-20-parseInt(N)*5); 
                                        _list[i][1].stroke();
                                    }
                                    catch (e)
                                    {
                                        continue
                                    }
                                }
                            }
                  
                }
              });
    }, 1000);
};
// var connectButton = document.getElementById("connect");
// connectButton.onclick = loopConnect;
