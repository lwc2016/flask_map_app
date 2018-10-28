$(document).ready(function(){
    var map = new BMap.Map("content");
    var point = new BMap.Point(116.404, 39.915);
    map.centerAndZoom(point, 15);
    map.enableScrollWheelZoom();

    var marker = new BMap.Marker(point);
    map.addOverlay(marker);
    marker.enableDragging();
    marker.addEventListener("dragging", function(event){
        setPotionForm(event.point);
    });

    // 切换省
    $("#provinceCode").change(function(){
        let provinceCode = $(this).val();
        let province = $(this).find("option:selected").text();
        $("#province").val(province);
        getCities(provinceCode);
        getPoint();
    });
    // 切换市
    $("#cityCode").change(function(){
        let cityCode = $(this).val();
        let city = $(this).find("option:selected").text();
        $("#city").val(city);
        getAreas(cityCode);
        getPoint()
    });
    // 切换区
    $("#areaCode").change(function(){
        let area = $(this).find("option:selected").text();
        $("#area").val(area);
        getPoint();
    });
    // 地址变化
    $("#address").on("input", function(){
       getPoint();
    });

    // 获取经纬度
    function getPoint(){
        let province = "";
        if($("#provinceCode").val()){
            province = $("#provinceCode").find("option:selected").text();
        }
        let city = "";
        if($("#cityCode").val()){
            city = $("#cityCode").find("option:selected").text();
        }
        let area = "";
        if($("#areaCode").val()){
            area = $("#areaCode").find("option:selected").text();
        }
        let address = $("#address").val();
        let _address = city + "" + area + "" + address;

        var myGeo = new BMap.Geocoder();
        myGeo.getPoint(_address, function(point){
		    if (point) {
			    map.centerAndZoom(point, 16);
			    setPotionForm(point);
                marker.setPosition(point);
		    }
	    }, city);
    }

    function setPotionForm(point){
        $("#longitude").val(point.lng);
        $("#latitude").val(point.lat);
    }
});