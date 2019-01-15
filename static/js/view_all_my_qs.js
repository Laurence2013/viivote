(function(){
  function getBaseUrl(){
    let url = location.href;
    let baseURL = url.substring(0, url.indexOf('/', 14));
    if (baseURL.indexOf('http://localhost') != -1) {
        let url = location.href;  // window.location.href;
        let pathname = location.pathname;  // window.location.pathname;
        let index1 = url.indexOf(pathname);
        let index2 = url.indexOf("/", index1 + 1);
        let baseLocalUrl = url.substr(0, index2);
        return baseLocalUrl + "/";
    } else {
        return baseURL + "/";
    }
  }
  let base_url = getBaseUrl();
  let edit_my_qs = 'edit_my_question'
  let http = new XMLHttpRequest()
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      let html = '';

      html += '<ul>';
      Object.values(results).forEach(function(result){
        let date_updated = result.question.date_updated.slice(0, -14);
        let new_date_format = function(datee){
          let date_split = datee.split("-");
          let year = date_split[0];
          let month = date_split[1];
          let day = date_split[2];
          return day + '/' + month + '/' + year;
        };
        
        //let test = 'key' + encodeURIComponent(result.question.id);
        //console.log(test);

        html += '<li>'+ result.question.question +' - <small>date added: '+ new_date_format(date_updated) +'</small></li>';
        html +='<li><b>Vote A: </b>'+ result.vote_a.vote +'</li>';
        html +='<li><b>Vote B: </b>'+ result.vote_b.vote +'</li>';
        html +='<li><b>Vote C: </b>'+ result.vote_c.vote +'</li>';
        html += '<small><a href="'+ base_url +'">Edit</a></small> | <small><a href="#">Delete</a></small>';
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
