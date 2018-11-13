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

    // 存放门店列表
    var shops = [];
    // 存放marker
    var markers = [];

    //var point = new BMap.Point(116.404, 39.915);
    //  初始化中心点
    //setCenter(point, 15);

    getShopList();

    // 获取门店列表
    function getShopList(){
        $.get("/api/device/list", {}, function(resp){
            if(resp.code == "0"){
                shops = resp.result || [];
                console.log(shops);
                shops.forEach((shop, index)=>{
                    // 以第一个数据为中心点
                    //let _point = new BMap.Point(shop.baidu_lng, shop.baidu_lat);
                    //var _position = new google.maps.LatLng(shop.google_lng, shop.google_lng);
                    if(index === 0){
                        setCenter(shop.google_lng, shop.google_lat);
                    }
                    setMarker(shop.google_lng, shop.google_lat);
                })
            }
        });
    }



    // 设置地点图标
    function setMarker(lng, lat){
        console.log("lat: ", lat);
        console.log("lng: ", lng);
        // 创建标记
        var marker=new google.maps.Marker({
            position: new google.maps.LatLng(lat, lng),
            //animation:google.maps.Animation.BOUNCE
            //draggable: true
        });
        marker.setMap(map);
    }

    // 设置中心点
    function setCenter(lng, lat){
        var position = new google.maps.LatLng(lat, lng);
        map.setCenter(position);
    }

    // 点击门店名称
    $(".shopName").click(function(){
       let index = $(this).data()["index"] - 1;
       let shop = shops[index];
       let _point = new BMap.Point(shop.baidu_lng, shop.baidu_lat);
       setCenter(_point, 12);
    });
});