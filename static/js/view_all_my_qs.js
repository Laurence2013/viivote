(function(){
  let http = new XMLHttpRequest()
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      console.log(results);
    }
  }
  http.open('GET', 'get_all_my_questions', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
