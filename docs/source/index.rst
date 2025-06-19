欢迎来到Bitdeck的文档!
=======================

**Bitdeck** 结合AI元素的开源软硬件的推进者，尤其在定位系统、机器人、嵌入式智能系统、动作捕捉和边缘AI等领域，
人工智能和机器人技术，在2025年有质的飞跃，会极大赋能各个行业，期待后续开源项目的快速推进。

飞行器 PK 机器狗
-------------------------

.. raw:: html

   <div style="text-align: center">
      <video width="100%" height="auto" controls autoplay muted loop>
         <source src="./_static/crazyflie_and_Unitree_Go2.mp4" type="video/mp4">
         Your browser does not support the video tag.
      </video>
   </div>

致谢家人
---------
.. note::

   感谢家人的陪伴，让我可以坚定信心的一直做下去!

支持客户
--------

.. raw:: html

   <!-- Leaflet 样式与脚本 -->
   <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
   <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

   <div id="map" style="width: 100%; height: 700px;"></div>

   <script>
       const map = L.map('map').setView([30.8617, 110.1954], 3.8);

       L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
           attribution: '&copy; OpenStreetMap contributors'
       }).addTo(map);

       // 不同类型高校使用不同颜色图标
       function getIcon(type) {
           const color = {
               "985": "red",
               "211": "blue",
               "world": "green",
               "other": "violet"
           }[type] || "blue";

           return L.icon({
               iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-${color}.png`,
               shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
               iconSize: [25, 41],
               iconAnchor: [12, 41],
               popupAnchor: [1, -34],
               shadowSize: [41, 41]
           });
       }

       const universities = [
           //🔴 985 高校
           {name: "北京航空航天大学", coords: [40.0005, 116.3479], type: "985"},
           {name: "北京理工大学", coords: [39.9570, 116.3160], type: "985"},
           {name: "上海交通大学", coords: [31.0255, 121.4331], type: "985"},
           {name: "浙江大学", coords: [30.2592, 120.0646], type: "985"},
           {name: "南京大学", coords: [32.0588, 118.7776], type: "985"},
           {name: "武汉大学", coords: [30.5385, 114.3598], type: "985"},
           {name: "中山大学", coords: [23.0993, 113.2997], type: "985"},
           {name: "西安交通大学", coords: [34.2468, 108.9973], type: "985"},
           {name: "哈尔滨工业大学", coords: [45.7390, 126.6800], type: "985"},
           {name: "中国科学技术大学", coords: [31.8409, 117.2644], type: "985"},
           {name: "重庆大学", coords: [29.5610, 106.5527], type: "985"},
           {name: "华南理工大学", coords: [23.1769, 113.4158], type: "985"},
           {name: "中南大学", coords: [27.8332, 112.9175], type: "985"},
           {name: "东南大学", coords: [32.0416, 118.7907], type: "985"},
           {name: "西北工业大学", coords: [34.2334, 108.9110], type: "985"},
           {name: "同济大学", coords: [31.2810, 121.5082], type: "985"},

           //🔵 211 高校
           {name: "西安电子科技大学", coords: [34.1299, 108.8370], type: "211"},
           {name: "中国地质大学", coords: [30.5053, 114.4145], type: "211"},
           {name: "西南大学", coords: [29.8297, 106.3967], type: "211"},
           {name: "南京理工大学", coords: [32.0920, 118.8219], type: "211"},
           {name: "北京科技大学", coords: [39.9886, 116.3604], type: "211"},
           {name: "华东师范大学", coords: [31.2285, 121.4116], type: "211"},
           {name: "苏州大学", coords: [31.2966, 120.6127], type: "211"},

           //🟢 世界级
           {name: "南方科技大学", coords: [22.5183, 113.9162], type: "world"},

           //🟢 世界级
           {name: "香港大学", coords: [22.2830, 114.1371], type: "world"},
           {name: "香港科技大学", coords: [22.3364, 114.2654], type: "world"},
           {name: "香港城市大学", coords: [22.3372, 114.1731], type: "world"},
           {name: "香港理工大学", coords: [22.3046, 114.1790], type: "world"},

           // 其他高校
           {name: "东北石油大学", coords: [46.6291, 125.0201], type: "other"},
           {name: "江苏科技大学", coords: [32.0682, 119.0000], type: "other"},
           {name: "中国民航大学", coords: [39.1239, 117.2180], type: "other"},
           {name: "西安建筑科技大学", coords: [34.2460, 108.9816], type: "other"},
           {name: "湖州师范学院", coords: [30.8510, 120.1030], type: "other"}
       ];

       universities.forEach(uni => {
           L.marker(uni.coords, {icon: getIcon(uni.type)})
               .addTo(map)
               .bindTooltip(uni.name, {
                   permanent: true,
                   direction: 'top',
                   offset: [0, -10],
                   className: 'university-label'
               }).openTooltip();
       });
   </script>

   <style>
   .university-label {
       background: rgba(255, 255, 255, 0.9);
       border: 1px solid #ccc;
       border-radius: 4px;
       padding: 2px 6px;
       font-size: 12px;
       font-weight: bold;
       white-space: nowrap;
       box-shadow: 0 1px 3px rgba(0,0,0,0.2);
       text-shadow: 0 0 2px white;
   }
   </style>



.. note::

   持续更新中

联系方式
--------

如果有需要交流可以加微信: 

.. figure:: ./_static/images/wechat_bitdeck.jpg
   :align: center
   :alt: 个人二维码
   :figclass: align-center

.. toctree::
   :maxdepth: 6

   bitcraze/client/client_list
   bitcraze/crazyflie/crazyflie_list
   bitcraze/crazyradio/crazyradio_list
   bitcraze/deck/deck_list
   bitcraze/swarm/swarm_list


