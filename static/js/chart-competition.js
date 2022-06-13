// dacon basic button event 2

$("#dacon-basic-button").click(function(){

    $("#basic-first").show();
    $("#basic-second").show();
    $("#basic-third").show();
    $("#basic-fourth").show();
    $("#total-first").hide();
    $("#total-second").hide();
    $("#total-third").hide();
    $("#total-fourth").hide();
});

// total competition button event 2

$("#total-competition-button").click(function(){
    $("#basic-first").hide();
    $("#basic-second").hide();
    $("#basic-third").hide();
    $("#basic-fourth").hide();
    $("#total-first").show();
    $("#total-second").show();
    $("#total-third").show();
    $("#total-fourth").show();
});

$("#total-first").hide();
$("#total-second").hide();
$("#total-third").hide();
$("#total-fourth").hide();