fetch("https://api.github.com/users/Shanta-Marasini/repos")
  .then((response) => response.json())
  .then((data) =>
    data.forEach((element) => {
      let single_div = document.createElement("div");
      let repoName = document.createElement("span");
      let icon = document.createElement("img");
      let a = document.createElement("a");

      single_div.setAttribute("id", "single-repo");

      icon.setAttribute("src", image);
      icon.setAttribute("alt", "the repo");
      icon.setAttribute("class", "repo-img");

      repoName.setAttribute("id", "repo-name");
      repoName.textContent = element.name;

      a.setAttribute("class", "repo-url");
      let url = element.html_url;
      a.setAttribute("href", url);
      a.setAttribute("target", "_blank");
      a.textContent = "Visit Me";

      let div = document.getElementById("repo-list-ul");
      single_div.append(icon, repoName, a);
      div.append(single_div);
    })
  );

document.getElementById("githublink").href = data["html_url"];
document.getElementById("repos").href = data["repos_url"];

