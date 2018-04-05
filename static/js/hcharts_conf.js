// 图表配置
var options = {
    chart: {
        type: 'line'                          //指定图表的类型，默认是折线图（line）
    },
    title: {
        text: null                  // 标题
    },
    xAxis: {
        categories: xxoo,  // x 轴分类
        tickmarkPlacement:"on",        // x 轴对齐方式
        title: {
            text: "最近七天阅读量"
        }
    },
    yAxis: {
        title: {
            text: null                  // y 轴标题
        },
        labels: {
            enabled: true
        },
        gridLineDashStyle: 'Dash'
    },
    series: [{                                // 数据列
        name: '阅读量',                   // 数据列名
        data: xxoo           // 数据
    }],
    legend: {
        enabled: false
    },
    credits: {
        enabled: false
    },
    plotOptions:{
        line: {
            dataLabels: {
                enabled:true
            }
        }
    }
};
// 图表初始化函数
var chart = Highcharts.chart('container', options);