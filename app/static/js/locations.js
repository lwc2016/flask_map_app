((window)=>{
    window.getCities = function(provinceCode){
       $.get("/api/getCities", {provinceCode: provinceCode}, function(resp){
           console.log(resp);
           if(resp.code == "0"){
               let options = resp.result.map(item=>"<option value='" + item.code + "'>" + item.name + "</option>");
               resetCityOption();
               resetAreaOption();
               $("#cityCode").append(options);
           }
       })
   };

   window.getAreas = function(cityCode){
       $.get("/api/getAreas", {cityCode: cityCode}, function(resp){
          console.log(resp);
          if(resp.code == "0"){
              let options = resp.result.map(item=>"<option value='" + item.code + "'>" + item.name + "</option>");
              resetAreaOption();
              $("#areaCode").append(options);
          }
       });
   };

   function resetCityOption(){
       $("#cityCode").find("option").remove();
       $("#cityCode").append("<option value=''>请选择市</option>");
   };

   function resetAreaOption(){
       $("#areaCode").find("option").remove();
       $("#areaCode").append("<option value=''>请选择区</option>");
   };
})(window);