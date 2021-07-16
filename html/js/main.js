eel.expose(output_logs)
function output_logs(values) {
  document.getElementById("log-output").value += values;
  document.getElementById("log-output").scrollTop = document.getElementById("log-output").scrollHeight;
}
async function search_character() {
  csv_name = document.getElementById("csv_name").value.trim();
  search_word = document.getElementById("search_word").value.trim();
  if (!csv_name) {
    alert("csvファイル名を入力してください。");
  } else if (!search_word) {
    alert("検索ワードを入力してください。");
  } else {
    await eel.search_character(csv_name, search_word);
  }
}
