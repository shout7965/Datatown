var chart_161 = c3.generate({
    bindto: '#chart-trend_161',
    data: {
        x: 'x',
        columns: []
    },
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                format: '%Y-%m-%d'
            }
        }
    }
});

$.ajax({

	method: "GET",
    url: "/job_trend_161"
}).done(function(response) {
    var dt_list_161 = [];
	var job_count_161 = [];

    // Array의 0번째 요소에 x 축의 이름과, 범례 이름 추가
    dt_list_161 = ['x',Object.keys(response)[Object.keys(response).length-1],Object.keys(response)[Object.keys(response).length-2],Object.keys(response)[Object.keys(response).length-3],Object.keys(response)[Object.keys(response).length-4],Object.keys(response)[Object.keys(response).length-5],Object.keys(response)[Object.keys(response).length-6],Object.keys(response)[Object.keys(response).length-7],Object.keys(response)[Object.keys(response).length-8],Object.keys(response)[Object.keys(response).length-9],Object.keys(response)[Object.keys(response).length-10]]
    job_count_161 = ['일자별 신규 채용공고 수', Object.values(response)[Object.values(response).length-1],Object.values(response)[Object.values(response).length-2],Object.values(response)[Object.values(response).length-3],Object.values(response)[Object.values(response).length-4],Object.values(response)[Object.values(response).length-5],Object.values(response)[Object.values(response).length-6],Object.values(response)[Object.values(response).length-7],Object.values(response)[Object.values(response).length-8],Object.values(response)[Object.values(response).length-9],Object.values(response)[Object.values(response).length-10]];

    console.log(dt_list_161, job_count_161);

	chart_161.load({
        columns: [dt_list_161, job_count_161]
    });
});

var chart_162 = c3.generate({
    bindto: '#chart-trend_162',
    data: {
        x: 'x',
        columns: []
    },
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                format: '%Y-%m-%d'
            }
        }
    }
});

$.ajax({

	method: "GET",
    url: "/job_trend_162"
}).done(function(response) {
    var dt_list_162 = [];
	var job_count_162 = [];

    // Array의 0번째 요소에 x 축의 이름과, 범례 이름 추가
    dt_list_162 = ['x',Object.keys(response)[Object.keys(response).length-1],Object.keys(response)[Object.keys(response).length-2],Object.keys(response)[Object.keys(response).length-3],Object.keys(response)[Object.keys(response).length-4],Object.keys(response)[Object.keys(response).length-5],Object.keys(response)[Object.keys(response).length-6],Object.keys(response)[Object.keys(response).length-7],Object.keys(response)[Object.keys(response).length-8],Object.keys(response)[Object.keys(response).length-9],Object.keys(response)[Object.keys(response).length-10]]
    job_count_162 = ['일자별 신규 채용공고 수', Object.values(response)[Object.values(response).length-1],Object.values(response)[Object.values(response).length-2],Object.values(response)[Object.values(response).length-3],Object.values(response)[Object.values(response).length-4],Object.values(response)[Object.values(response).length-5],Object.values(response)[Object.values(response).length-6],Object.values(response)[Object.values(response).length-7],Object.values(response)[Object.values(response).length-8],Object.values(response)[Object.values(response).length-9],Object.values(response)[Object.values(response).length-10]];

    console.log(dt_list_162, job_count_162);

	chart_162.load({
        columns: [dt_list_162, job_count_162]
    });
});

$("#bigdata-chart-button").click(function(){
    $("#chart-trend_162").hide();
    $("#chart-trend_161").show();
});

$("#ai-chart-button").click(function(){
    $("#chart-trend_161").hide();
    $("#chart-trend_162").show();
});

$("#chart-trend_162").hide();