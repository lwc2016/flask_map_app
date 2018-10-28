$(document).ready(function(){
    // 全局变量
    var map = new BMap.Map("content");
    map.enableScrollWheelZoom();

    // 存放门店列表
    var shops = [];
    // 存放marker
    var markers = [];

    var point = new BMap.Point(116.404, 39.915);
    //  初始化中心点
    setCenter(point, 15);

    getShopList();

    // 获取门店列表
    function getShopList(){
        $.get("/api/shop/list", {}, function(resp){
            if(resp.code == "0"){
                shops = resp.result || [];
                shops.forEach((shop, index)=>{
                    // 以第一个数据为中心点
                    let _point = new BMap.Point(shop.longitude, shop.latitude);
                    if(index === 0){
                        setCenter(_point, 12)
                    }
                    setMarker(shop);
                })
            }
        });
    }



    // 设置地点图标
    function setMarker(shop){
        let point = new BMap.Point(shop.longitude, shop.latitude);
        let marker = new BMap.Marker(point);
        map.addOverlay(marker);
        var opts = {
	        width : 200,     // 信息窗口宽度
	        height: 80,     // 信息窗口高度
	        title : shop.name , // 信息窗口标题
	        enableMessage:true,//设置允许信息窗发送短息
	        message:"亲耐滴，晚上一起吃个饭吧？戳下面的链接看下地址喔~"
        };
        let _address = shop.province + "" + shop.city + ""  + shop.area + "，" + shop.address;
        var infoWindow = new BMap.InfoWindow("地址：" + _address, opts);
        marker.addEventListener("click", function(){
            map.openInfoWindow(infoWindow, point);
        });
        markers.push(marker);
    }

    // 设置中心点
    function setCenter(point, scale){
        map.centerAndZoom(point, scale);
    }

    // 点击门店名称
    $(".shopName").click(function(){
       let index = $(this).data()["index"] - 1;
       let shop = shops[index];
       let _point = new BMap.Point(shop.longitude, shop.latitude);
       setCenter(_point, 12);
    });
});
