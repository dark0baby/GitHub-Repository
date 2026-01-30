fetch("../data/all_news.json")
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("news");
    data.slice(-10).reverse().forEach(item => {
      const div = document.createElement("div");
      div.className = "card";
      div.innerHTML = `
        <b>${item.what}</b><br/>
        Sector: ${item.sectors.join(", ")}<br/>
        RBI Impact: ${item.rbi_repo}<br/>
        Stocks: ${item.large_cap.join(", ")}
      `;
      container.appendChild(div);
    });
  });
