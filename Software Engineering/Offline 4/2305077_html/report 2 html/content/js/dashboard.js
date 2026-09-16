/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 77.85714285714286, "KoPercent": 22.142857142857142};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.7785714285714286, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "/login-1"], "isController": false}, {"data": [0.98, 500, 1500, "/login"], "isController": false}, {"data": [1.0, 500, 1500, "/login-0"], "isController": false}, {"data": [1.0, 500, 1500, "/api/download/256-56"], "isController": false}, {"data": [0.2, 500, 1500, "/courses-39"], "isController": false}, {"data": [0.28, 500, 1500, "/notices"], "isController": false}, {"data": [0.99, 500, 1500, "/"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 700, 155, 22.142857142857142, 121.12571428571428, 14, 500, 69.5, 317.0, 361.7999999999997, 452.99, 7.0066563235073325, 523.7952421988389, 3.731083591912317], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["/login-1", 100, 0, 0.0, 50.03000000000001, 24, 178, 47.0, 68.0, 87.89999999999998, 177.20999999999958, 1.008288128415576, 107.35057603185686, 0.5445149755994273], "isController": false}, {"data": ["/login", 100, 2, 2.0, 111.42, 62, 258, 107.5, 139.8, 155.69999999999993, 257.6399999999998, 1.0074957685177721, 107.77193058543061, 1.0576737804263723], "isController": false}, {"data": ["/login-0", 100, 0, 0.0, 60.680000000000014, 31, 172, 61.0, 82.80000000000001, 87.0, 171.28999999999962, 1.0080645161290323, 0.5060011340725806, 0.5138766381048387], "isController": false}, {"data": ["/api/download/256-56", 100, 0, 0.0, 39.550000000000004, 28, 154, 31.0, 58.50000000000003, 84.44999999999987, 153.86999999999995, 1.0083898031623104, 258.4225364406865, 0.508133924249758], "isController": false}, {"data": ["/courses-39", 100, 80, 80.0, 258.0399999999999, 176, 426, 238.5, 328.9, 349.84999999999997, 425.3599999999997, 1.00664384940608, 43.65432951228105, 0.3961694055768069], "isController": false}, {"data": ["/notices", 100, 72, 72.0, 288.76000000000005, 110, 500, 305.5, 440.70000000000005, 453.95, 499.8399999999999, 1.0061273153504846, 7.386782379692326, 0.38908829773319514], "isController": false}, {"data": ["/", 100, 1, 1.0, 39.399999999999984, 14, 283, 34.5, 51.900000000000006, 59.89999999999998, 281.7899999999994, 1.010243872870911, 2.4013023306326144, 0.34727133129937565], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["The operation lasted too long: It took 204 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 323 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 390 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 452 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 236 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 313 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 405 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 370 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 283 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 214 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 278 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 318 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, 2.5806451612903225, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 484 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 395 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 234 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 273 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 224 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 244 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 202 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 221 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 311 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 350 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 266 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 326 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 243 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 222 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 305 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 383 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 379 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 316 milliseconds, but should not have lasted longer than 200 milliseconds.", 5, 3.225806451612903, 0.7142857142857143], "isController": false}, {"data": ["The operation lasted too long: It took 218 milliseconds, but should not have lasted longer than 200 milliseconds.", 3, 1.935483870967742, 0.42857142857142855], "isController": false}, {"data": ["The operation lasted too long: It took 212 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 290 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 429 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 320 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 315 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 500 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 280 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 408 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 213 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 335 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, 2.5806451612903225, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 461 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 248 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 219 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 412 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 223 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 262 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 297 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 209 milliseconds, but should not have lasted longer than 200 milliseconds.", 3, 1.935483870967742, 0.42857142857142855], "isController": false}, {"data": ["The operation lasted too long: It took 203 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, 2.5806451612903225, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 418 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 310 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 364 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 438 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 345 milliseconds, but should not have lasted longer than 200 milliseconds.", 3, 1.935483870967742, 0.42857142857142855], "isController": false}, {"data": ["The operation lasted too long: It took 258 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 422 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 306 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 386 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 329 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 240 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 319 milliseconds, but should not have lasted longer than 200 milliseconds.", 3, 1.935483870967742, 0.42857142857142855], "isController": false}, {"data": ["The operation lasted too long: It took 354 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 334 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 441 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 453 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 289 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 339 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 235 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 426 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 421 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 312 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 225 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 299 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 317 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, 2.5806451612903225, 0.5714285714285714], "isController": false}, {"data": ["The operation lasted too long: It took 401 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 443 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 398 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 314 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 349 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 227 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 270 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 468 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 208 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 247 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 205 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 414 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 237 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 327 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 347 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 362 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 207 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 358 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 211 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 337 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 331 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 217 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 201 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 434 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 216 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 206 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, 1.2903225806451613, 0.2857142857142857], "isController": false}, {"data": ["The operation lasted too long: It took 220 milliseconds, but should not have lasted longer than 200 milliseconds.", 3, 1.935483870967742, 0.42857142857142855], "isController": false}, {"data": ["The operation lasted too long: It took 381 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 328 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 415 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}, {"data": ["The operation lasted too long: It took 454 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, 0.6451612903225806, 0.14285714285714285], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 700, 155, "The operation lasted too long: It took 316 milliseconds, but should not have lasted longer than 200 milliseconds.", 5, "The operation lasted too long: It took 318 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, "The operation lasted too long: It took 335 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, "The operation lasted too long: It took 203 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, "The operation lasted too long: It took 317 milliseconds, but should not have lasted longer than 200 milliseconds.", 4], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": ["/login", 100, 2, "The operation lasted too long: It took 222 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, "The operation lasted too long: It took 258 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["/courses-39", 100, 80, "The operation lasted too long: It took 318 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, "The operation lasted too long: It took 316 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, "The operation lasted too long: It took 203 milliseconds, but should not have lasted longer than 200 milliseconds.", 4, "The operation lasted too long: It took 317 milliseconds, but should not have lasted longer than 200 milliseconds.", 3, "The operation lasted too long: It took 220 milliseconds, but should not have lasted longer than 200 milliseconds.", 3], "isController": false}, {"data": ["/notices", 100, 72, "The operation lasted too long: It took 335 milliseconds, but should not have lasted longer than 200 milliseconds.", 3, "The operation lasted too long: It took 453 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 234 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 207 milliseconds, but should not have lasted longer than 200 milliseconds.", 2, "The operation lasted too long: It took 218 milliseconds, but should not have lasted longer than 200 milliseconds.", 2], "isController": false}, {"data": ["/", 100, 1, "The operation lasted too long: It took 283 milliseconds, but should not have lasted longer than 200 milliseconds.", 1, "", "", "", "", "", "", "", ""], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
