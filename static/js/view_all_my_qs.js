(function(){
  let http = new XMLHttpRequest()
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      let html = '';

      html += '<ul>';
      Object.values(results).forEach(function(result){
        console.log(result);
        html += '<li>'+ result.question.question+' - <small>date added: </small>'+ result.question.date_updated.slice(0, -14)+'</li>';
        html +='<li><b>Vote A: </b>'+ result.vote_a.vote +'</li>';
        html +='<li><b>Vote B: </b>'+ result.vote_b.vote +'</li>';
        html +='<li><b>Vote C: </b>'+ result.vote_c.vote +'</li>';
        html += '<hr>';
      });
      html += '</ul>';
      document.getElementById('get_all_questions').innerHTML = html;
    }
  }
  http.open('GET', 'get_all_my_questions', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
