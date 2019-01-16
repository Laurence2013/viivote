(function(){
  let http = new XMLHttpRequest();
  http.onreadystatechange = function(){
    if(http.readyState == 4 && http.status == 200){
      let results = JSON.parse(http.responseText);
      console.log(results);
      let html = '';
      html += '<table style="width:50%>"';
      html += '<tr>';
      html += '<th>Your question</th>';
      html += '<th>Edit and update a question (optional)</th>';
      html += '</tr>';
      html += '<tr>';
      for(let result in results){
        if(results[result].question !== undefined){
          html += '<td>'+ results[result].question + '</td>';
          html += '<td><input type="hidden" name="question_id" value="'+ results[result].id +'"><input type="text" name="question" value="" placeholder="Edit your question"></td>';
        }
      }
      html += '</tr>';
      html += '<tr>'
      html += '<th>Your votes</th>';
      html += '<th>Edit and update any vote or all votes (optional)</th>';
      html += '</tr>';
      for(let result in results){
        html += '<tr>';
        if(results[result].vote_type !== undefined){
          html += '<td>'+ results[result].vote.vote +'</td>';
          html += '<td><input type="hidden" name="'+ results[result].vote_type +'" value="'+ results[result].vote.id +'"><input type="text" name="'+ results[result].vote_abc +'" value="" placeholder="Edit your vote"></td>';
        }
        html += '</tr>';
      }
      html += '</table>';
      document.getElementById('edit_all_my_questions').innerHTML = html;
    }
  }
  http.open('GET', 'get_edit_all_my_questions', true);
  http.setRequestHeader('Content-type', 'application/json', true);
  http.send();
})();
