$("#hide-button").click(function(){
    $("#p-1").hide();
});

$("#show-button").click(function(){
    $("#p-1").show();
});

$("#p-2").hide();
$("#p-3").hide();

$("#show-p-2-button").click(function(){
    $("#p-2").show();
    $("#p-3").hide();
});

$("#show-p-3-button").click(function(){
    $("#p-2").hide();
    $("#p-3").show();
});

$("#get-text-button").click(function(){
    var str = $("#p-4").text();
    alert(str);
});

$("#set-text-button").click(function(){
    $("#p-4").text("<i>this is</i> <b>content</b> 4-2");
});

$("#get-html-button").click(function(){
    var str = $("#p-5").html();
    alert(str);
});

$("#set-html-button").click(function(){
    $("#p-5").html("<i>this is</i> <b>content</b> 5-2");
});

$("#append-text-button").click(function(){
    $("#p-6").append(" this is new content");
});

$("#append-html-button").click(function(){
    $("#p-6").append(" this is <i>new</i> <b>content</b>");
});

$("#prepend-text-button").click(function(){
    $("#p-7").prepend(" this is new content ");
});

$("#prepend-html-button").click(function(){
    $("#p-7").prepend(" this is <i>new</i> <b>content</b> ");
});

$("#2016-button").click(function(){
    $("#2016_nouns").show();
    $("#2017_nouns").hide();
    $("#2018_nouns").hide();
    $("#2019_nouns").hide();
    $("#2020_nouns").hide();
    $("#2021_nouns").hide();
    $("#2022_nouns").hide();
});

$("#2017-button").click(function(){
    $("#2016_nouns").hide();
    $("#2017_nouns").show();
    $("#2018_nouns").hide();
    $("#2019_nouns").hide();
    $("#2020_nouns").hide();
    $("#2021_nouns").hide();
    $("#2022_nouns").hide();
});

$("#2018-button").click(function(){
    $("#2016_nouns").hide();
    $("#2017_nouns").hide();
    $("#2018_nouns").show();
    $("#2019_nouns").hide();
    $("#2020_nouns").hide();
    $("#2021_nouns").hide();
    $("#2022_nouns").hide();
});

$("#2019-button").click(function(){
    $("#2016_nouns").hide();
    $("#2017_nouns").hide();
    $("#2018_nouns").hide();
    $("#2019_nouns").show();
    $("#2020_nouns").hide();
    $("#2021_nouns").hide();
    $("#2022_nouns").hide();
});

$("#2020-button").click(function(){
    $("#2016_nouns").hide();
    $("#2017_nouns").hide();
    $("#2018_nouns").hide();
    $("#2019_nouns").hide();
    $("#2020_nouns").show();
    $("#2021_nouns").hide();
    $("#2022_nouns").hide();
});

$("#2021-button").click(function(){
    $("#2016_nouns").hide();
    $("#2017_nouns").hide();
    $("#2018_nouns").hide();
    $("#2019_nouns").hide();
    $("#2020_nouns").hide();
    $("#2021_nouns").show();
    $("#2022_nouns").hide();
});

$("#2022-button").click(function(){
    $("#2016_nouns").hide();
    $("#2017_nouns").hide();
    $("#2018_nouns").hide();
    $("#2019_nouns").hide();
    $("#2020_nouns").hide();
    $("#2021_nouns").hide();
    $("#2022_nouns").show();
});

    $("#2016_nouns").hide();
    $("#2017_nouns").hide();
    $("#2018_nouns").hide();
    $("#2019_nouns").hide();
    $("#2020_nouns").hide();
    $("#2021_nouns").hide();