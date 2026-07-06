const pageSize = 50;

let data = {};
let currentPage = 1;

async function loadData() {

    const response = await fetch("data/result.json");

    data = await response.json();

    document.getElementById("update_time").textContent = data.update_time;
    document.getElementById("scan_count").textContent = data.scan_count;
    document.getElementById("count").textContent = data.count + " 檔";

    renderPage(1);

}

function renderPage(page) {

    currentPage = page;

    const stockList = document.getElementById("stock-list");

    stockList.innerHTML = "";

    const start = (page - 1) * pageSize;
    const end = start + pageSize;

    const stocks = data.stocks.slice(start, end);

    stocks.forEach(stock => {

        stockList.innerHTML += `

        <div style="
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            background: #fff;
        ">

            <h3>${stock.code} ${stock.name}</h3>

            <p>
                收盤價：${Number(stock.close).toFixed(2)}
            </p>

            <p>
                昨日最高：${Number(stock.high).toFixed(2)}
            </p>

            <p>
                OSC：
                <span
                    style="
                        color: ${stock.osc >= 0 ? "#d32f2f" : "#2e7d32"};
                        font-weight: bold;
                    "
                >
                    ${Number(stock.osc).toFixed(3)}
                </span>
            </p>

        </div>

        `;

    });

    renderPagination();

}

function renderPagination() {

    const totalPages = Math.ceil(data.stocks.length / pageSize);

    let html = "";

    // 上一頁
    if (currentPage > 1) {

        html += `
            <button
                onclick="renderPage(${currentPage - 1})"
                style="
                    width: 42px;
                    height: 42px;
                    border-radius: 10px;
                    border: 1px solid #d0d0d0;
                    background: white;
                    font-size: 18px;
                    cursor: pointer;
                "
            >
                ◀
            </button>
        `;

    }

    // 要顯示的頁碼範圍
    let startPage = Math.max(1, currentPage - 2);
    let endPage = Math.min(totalPages, currentPage + 2);

    // 如果靠近開頭
    if (currentPage <= 3) {

        endPage = Math.min(5, totalPages);

    }

    // 如果靠近結尾
    if (currentPage >= totalPages - 2) {

        startPage = Math.max(1, totalPages - 4);

    }

    // 頁碼按鈕
    for (let i = startPage; i <= endPage; i++) {

        if (i === currentPage) {

            html += `
                <button
                    style="
                        width: 42px;
                        height: 42px;
                        border-radius: 10px;
                        border: none;
                        background: #2563eb;
                        color: white;
                        font-size: 18px;
                        font-weight: bold;
                    "
                >
                    ${i}
                </button>
            `;

        } else {

            html += `
                <button
                    onclick="renderPage(${i})"
                    style="
                        width: 42px;
                        height: 42px;
                        border-radius: 10px;
                        border: 1px solid #d0d0d0;
                        background: white;
                        font-size: 18px;
                        cursor: pointer;
                    "
                >
                    ${i}
                </button>
            `;

        }

    }

    // 下一頁
    if (currentPage < totalPages) {

        html += `
            <button
                onclick="renderPage(${currentPage + 1})"
                style="
                    width: 42px;
                    height: 42px;
                    border-radius: 10px;
                    border: 1px solid #d0d0d0;
                    background: white;
                    font-size: 18px;
                    cursor: pointer;
                "
            >
                ▶
            </button>
        `;

    }

    document.getElementById("pagination").innerHTML = `
        <div
            style="
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 10px;
                margin: 25px 0;
                flex-wrap: wrap;
            "
        >
            ${html}
        </div>
    `;

}

loadData();