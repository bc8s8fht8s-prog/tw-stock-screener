async function loadData() {

    const response = await fetch("data/result.json");

    const data = await response.json();

    document.getElementById("update_time").textContent = data.update_time;
    document.getElementById("scan_count").textContent = data.scan_count;
    document.getElementById("count").textContent = data.count + " 檔";

    const stockList = document.getElementById("stock-list");

    stockList.innerHTML = "";

    data.stocks.forEach(stock => {

        stockList.innerHTML += `
        <div style="
            border:1px solid #ddd;
            border-radius:10px;
            padding:15px;
            margin:10px 0;
            background:#fff;
        ">

            <h3>${stock.code} ${stock.name}</h3>

            <p>收盤價：${Number(stock.close).toFixed(2)}</p>

            <p>昨日最高：${Number(stock.high).toFixed(2)}</p>

            <p>OSC：${Number(stock.osc).toFixed(3)}</p>

        </div>
        `;

    });

}

loadData();