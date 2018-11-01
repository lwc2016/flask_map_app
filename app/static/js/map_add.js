$(document).ready(function(){
    var mapType = google.maps.MapTypeId.ROADMAP;
    var lat = 39.915168, lng = 116.403875, zoom = 10;

    var position = new google.maps.LatLng(lat, lng);
    var mapOptions = {
        center: position,  //地图的中心点
        zoom: zoom,               　　　　　　　　　　//地图缩放比例
        mapTypeId: mapType,       　　　　　　　　　　//指定地图展示类型：卫星图像、普通道路
        scrollwheel: true          　　　　　　　　　 //是否允许滚轮滑动进行缩放
    };
    // 创建地图
    var map = new google.maps.Map(document.getElementById("map"), mapOptions); //创建谷歌地图


    // 创建标记
    var marker=new google.maps.Marker({
        position: new google.maps.LatLng(lat, lng),
        //animation:google.maps.Animation.BOUNCE
        //draggable: true
    });

    marker.setMap(map);



    // 切换省
    $("#provinceCode").change(function(){
        let provinceCode = $(this).val();
        let province = $(this).find("option:selected").text();
        $("#province").val(province);
        getCities(provinceCode);
        getPosition();
    });
    // 切换市
    $("#cityCode").change(function(){
        let cityCode = $(this).val();
        let city = $(this).find("option:selected").text();
        $("#city").val(city);
        getAreas(cityCode);
        getPosition()
    });
    // 切换区
    $("#areaCode").change(function(){
        let area = $(this).find("option:selected").text();
        $("#area").val(area);
        getPosition();
    });
// 地址变化
    $("#address").on("input", function(){
        getPosition();
    });



    function getPosition(){
        console.log("----ok-----")
        var province = $("#province").val();
        var city = $("#city").val();
        var area = $("#area").val();
        var address = $("#address").val();
        var _address = province + "" + city + "" + area + "" + address;
        var geocoder = new google.maps.Geocoder();

        console.log(_address);
        // 解析地址
        geocoder.geocode( { 'address': _address}, function(results, status) {
            console.log(results);
            if (status == google.maps.GeocoderStatus.OK) {
                console.log(results[0].geometry.location.lat());
                var lat = results[0].geometry.location.lat();
                var lng = results[0].geometry.location.lng();

                setCenter(lat, lng);
            } else {
                console.log("Geocode was not successful for the following reason: " + status);
            }
        });
    }


    function setCenter(lat, lng){
        var position = new google.maps.LatLng(lat, lng);
        map.setCenter(position);
        marker.setPosition(position);
        console.log("lat: ", lat);
        console.log("lng: ", lng);
        $("#longitude").val(lng);
        $("#latitude").val(lat);
    }
});
