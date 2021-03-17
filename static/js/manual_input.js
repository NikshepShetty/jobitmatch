$(function(){
    $technicals='';
    $('.technical').tokenize2();
    $('.technical').on("tokenize:tokens:add", function (event, value, text){
        $technicals=$technicals+text+',';
        document.getElementById("id_technicals").value = $technicals;
    });

});