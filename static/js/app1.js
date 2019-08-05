//去重函数
function data_1(data,) {
    var data_1 =[];
    for (var k=0;k<data.length;k++){
        data_1.push(data[k])
    }
    for (var i=0;i<data_1.length;i++){
        for (var j=i+1;j<data_1.length;j++){
            if( data_1[i].device ===data_1[j].device){
                data_1.splice(j,1);
                j=j-1;
            }
        }
    }
    var data_2 =[];
    for (var l=0;l<data_1.length;l++){
        data_2.push(data_1[l].device)
    }
    return data_2;
}  //设备降重
function data_2(data,) {
    var data_1 =[];
    for (var k=0;k<data.length;k++){
        data_1.push(data[k])
    }
    for (var i=0;i<data_1.length;i++){
        for (var j=i+1;j<data_1.length;j++){
            if( data_1[i].days ===data_1[j].days){
                data_1.splice(j,1);
                j=j-1;
            }
        }
    }
    var data_2 =[];
    for (var l=0;l<data_1.length;l++){
        data_2.push(data_1[l].days)
    }
    return data_2;
} //时间降重
//时间提取函数
function time_data_1(data,) {
    var data_1 =[];
    for (var k=0;k<data.length;k++){
        var a = data[k].time.split(",");
        data_1.push(a);
    }
    var data_2 =[];
    for (var l=0;l<data_1.length;l++){
        var b = data_1[l][1].split(" ");
        data_2.push(b)
    }
    var data_3 =[];
    for (var m=0;m<data_2.length;m++){
        var c ={};
        c.week = data_1[m][0];
        c.days = data_2[m][3]+"-"+data_2[m][2]+"-"+data_2[m][1];
        data_3.push(c)
    }
    // for (var i=0;i<data_1.length;i++){
    //     for (var j=i+1;j<data_1.length;j++){
    //         if( data_1[i].time ===data_1[j].time){
    //             data_1.splice(j,1);
    //             j=j-1;
    //         }
    //     }
    // }
    return data_3;

}
function time_data_2(data,) {
    var data_1 =[data.time.split(",")];
    var data_2 =[];
    for (var l=0;l<data_1.length;l++){
        var b = data_1[l][1].split(" ");
        data_2.push(b)
    }
    var data_3 =[];
    for (var m=0;m<data_2.length;m++){
        var c ={};
        c.week = data_1[m][0];
        c.days = data_2[m][3]+"-"+data_2[m][2]+"-"+data_2[m][1];
        data_3.push(c)
    }
    // for (var i=0;i<data_1.length;i++){
    //     for (var j=i+1;j<data_1.length;j++){
    //         if( data_1[i].time ===data_1[j].time){
    //             data_1.splice(j,1);
    //             j=j-1;
    //         }
    //     }
    // }
    return data_3;

}
//数据的筛选
//按照设备筛选
function filter(data,a) {
        var data_filter_1=[];
        for (var i=0;i<data.length;i++){
            if(a===data[i].device){
                data_filter_1.push(data[i])
            }
        }
        return data_filter_1;
}
function filter1(data,b) {
    var data_filter_2=[];
    for (var j=0;j<data.length;j++){
        const b1 = time_data_2(data[j]);
        console.log(b1);
        if(b===b1[0].days){
            data_filter_2.push(data[j])
        }
    }
    return data_filter_2
}

var app = angular.module('myApp',[]);
app.controller("myCtrl",['$scope','$http',function ($scope,$http) {
    $scope.title = '数据的显示';
    $scope.name1 = "按设备进行筛选";
    $scope.seen = false;
    $scope.seens = false;
    window.onload = function () {
        $http.get('http://10.199.172.228:8989/data/record').success(function (doc) {
            //获取数据，并将数据赋值给lists1列表，然后绑定到前端的页面表格中
            console.log(doc);
            $scope.lists1 = doc;
        })
    };
    $("#li1").click(function () {
        $(this).attr('class', "active");
        $("#li2").attr('class', '');
        $("#li3").attr('class', '');
        $("#li4").attr('class', '');
        $scope.title = '全数据的显示';
        $scope.seens = false;
        $scope.seen = false;
        // console.log(title);
        $http.get('http://10.199.172.228:8989/data/record').success(function (doc) {
            $scope.lists1 =doc;
            //按钮1
        })
    });
    $("#li2").click(function () {
        $(this).attr('class', "active");
        $("#li1").attr('class', '');
        $("#li3").attr('class', '');
        $("#li4").attr('class', '');
        $http.get('http://10.199.172.228:8989/data/record').success(function (doc) {
            $scope.lists1 =doc;
            $scope.device ='';
            $scope.seens = false;
            $scope.seen = true;
            $scope.title = '按设备筛选：';
            $scope.data_1 = data_1(doc);
            $scope.filter = function(){
                $scope.lists1 =(filter(doc,$scope.device));
            };
        })
    });
    //按钮3
    $("#li3").click(function () {
        var title = "请输入时间的筛选条件：";
        $(this).attr('class', "active");
        $("#li2").attr('class', '');
        $("#li4").attr('class', '');
        $scope.seen = true;
        $scope.seens = false;
        $("#li1").attr('class', '');
        $http.get('http://10.199.172.228:8989/data/record').success(function (doc) {
            $scope.lists1 =doc;
            $scope.data_1 =data_2(time_data_1(doc));
            $scope.title = title;

            $scope.filter = function(){

                $scope.lists1 =(filter1(doc,$scope.device));
            };
            //按钮1
        })
    });
    $("#li4").click(function () {
        $(this).attr('class', "active");
        $("#li2").attr('class', '');
        $("#li3").attr('class', '');
        $("#li1").attr('class', '');
        $scope.seens = true;
        $scope.seen = false;
        $http.get('http://10.199.172.228:8989/data/record').success(function (doc) {
            $scope.lists1 =doc;
        })
    });
}]);