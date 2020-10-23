function sayGoodbye() {
  alert("로그아웃 되었습니다.")
  document.location.href="/logout"
}
function daydate(){ //년과 월에 따라 마지막 일 구하기
  var day_data = $('#theday').serialize();
  $.ajax({
    type: 'POST'
    url : "/daydata"
    data : day_data,
    success:function(result){
      data=result.datalist;
      alert("result="+result)
    },
    error:function(xtr,status,error){
      alert(xtr+":"+status+":"+error)
    }
  });
}
