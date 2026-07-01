# 1.6x 버전 업데이트

## - 업데이트 내역 -

### 2.22.0 (2026/01/12)
#### 1. 시곡면 분석 정확도 향상
  - [시곡면 분석](https://sandbox.egiscloud.com/code/main.do?id=analysis_building_height_regulation) 정확도 향상 및 0~360도 범위 확장<br>
<img width="916" height="690" alt="image" src="https://github.com/user-attachments/assets/f091e9f7-1fd9-4a67-8dd6-f2d738cdfd96" />

#### 2. 1인칭 카메라 비디오 텍스쳐 기능 지원 중단
  - 기존 1인칭 카메라 비디오 텍스쳐 기능은 2025년까지 지원합니다. 
  - JSCamera 클래스의 삭제 API ---------> JSVideoObject 클래스의 대체 API 
    - setVideoInfo ---------> createVideo
    - clearVideo -----------> clearTexture
  - JSCamera 클래스의 삭제 property ---------> JSVideoObject 클래스의 대체 property
    - videoStreaming ---------------> videoStreaming
    - videoFar -----------------------> far
    - videoFovX ---------------------> fovX
    - videoFovY ---------------------> fovY
    - videoAlpha --------------------> alpha
    - videoAxisX --------------------> axisX
    - videoAxisY --------------------> axisY
    - videoZoom --------------------> zoom
    - videoFarPlane -----------------> background
    - videoResolution ---------------> resolution
    - videoObjectMapping ---------> objectMapping
    - videoIsplayer ------------------> isPlayer

  - 비디오 객체  [비디오 객체](https://sandbox.egiscloud.com/code/main.do?id=object_video), [전광판](https://sandbox.egiscloud.com/code/main.do?id=object_ledboard), [RTT 비디오](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_rtt_video_image_texture)를 참고하시기 바랍니다.

#### 3. 건물 레이어 limit boundary 옵션 추가
  * 건물 레이어 boundaryLimit에 mode: "exclude" 옵션을 추가해 경계 내부를 제외하고 외부 오브젝트만 로드할 수 있도록 개선했습니다.
  * 아래와 같이 설정하는 경우 바운더리 외 건물이 로드됩니다.
    ``` javascript
    const boundary = [
          [126.93005255915998, 37.529214172573376],
          [126.94102835336719, 37.52029412432422],
          [126.93891529125652, 37.51798498831805],
          [126.92841620055285, 37.516978366894115],
          [126.92514862234246, 37.51770012779483],
          [126.91756299430655, 37.521708873949606],
    ];

    Module.getTileLayerList().createXDServerLayer({
          ...
          boundaryLimit: {
            mode: "exclude",
            rings: boundary
          }
    });
    ```
  * 아래와 같이 설정하는 경우 바운더리 내부 건물만 로드됩니다. (기존 방식과 동일)
    ``` javascript
    const boundary = [
          [126.93005255915998, 37.529214172573376],
          [126.94102835336719, 37.52029412432422],
          [126.93891529125652, 37.51798498831805],
          [126.92841620055285, 37.516978366894115],
          [126.92514862234246, 37.51770012779483],
          [126.91756299430655, 37.521708873949606],
    ];

    Module.getTileLayerList().createXDServerLayer({
          ...
          boundaryLimit: {
            mode: "include",
            rings: boundary
          }
    });
    ```
* exclude/include 옵션이 없는 경우 include 타입으로 자동 지정되어 바운더리 내부 건물만 로드됩니다.

#### 4. 엔진 상태 체크 옵션 추가
```javascript
Module.initialize({
	.
	.
	.
	ping: enginePing
});

function enginePing(e) {
	console.log(e);
}
```

#### 5. 수평 이동 위치 반환 API 추가
* 전후좌우 방향으로 특정 거리만큼 수평 이동한 좌표를 반환하는 API가 추가되었습니다.
  ```javascript
  var camera = Module.getViewCamera();
  camera.getPanMoveLocation(moveType, distance);
  // moveType : 0(front), 1(back), 2(left), 3(right)
  ```

#### 6. 1인칭 카메라 모드 높이 설정 API 추가
* 1인칭 카메라 모드에서 카메라의 높이를 설정하는 API가 추가되었습니다.
  ```javascript
  var camera = Module.getViewCamera();
  camera.setPersonHeight(1.5);
  ```

#### 7. 플레이어 모드 천장 설정 API 추가
* 플레이어 모드에서 천장 고도를 설정하여 점프 시 천장에 부딪히도록 하는 API가 추가되었습니다.
  ```javascript
  var camera = Module.getViewCamera();
  camera.setCeiling() // 천장 설정 해제
  camera.setCeiling(10.0); // 천장 고도 설정
  ```
  
### 2.21.0 (2025/12/01)
#### 1. 카메라 타겟 좌표 반환 API 추가
- 카메라 이동 애니메이션이 적용된 상태에서 카메라의 최종 목적지 좌표를 반환하는 API가 추가되었습니다.
```javascript
var pos = Module.getViewCamera().getTargetLocation();
```

#### 2. 카메라 플레이어 모드 추가
- 1인칭 카메라에 플레이어 모드(물리 기반)가 추가되었습니다.
- 이 모드에서는 점프 및 중력 낙하 효과가 자연스럽게 적용됩니다.
```javascript
var camera = Module.getViewCamera();
camera.setPlayerMode(true); // 플레이어 모드 활성화
camera.setPlayerMode(false); // 플레이어 모드 비활성화
```

#### 3. 카메라 점프 기능 API 추가
- 플레이어 모드에서 카메라가 점프 동작을 수행할 수 있는 API가 추가되었습니다.
- 점프 세기(jumpForce), 중력(gravity), 시간 간격(timeStep)을 조절할 수 있습니다.
- [샌드박스 샘플](https://sandbox.egiscloud.com/code/main.do?id=camera_jump_outdoor)
```javascript
var camera = Module.getViewCamera();
camera.setJumpForce(30.0); // 기본값 10.0
camera.setGravity(9.8); // 기본값 9.8
camera.setTimeStep(0.06); // 기본값 0.05
camera.jump();
```

#### 4. 카메라 지면 감지 API 추가
- 1인칭 카메라가 현재 지면에 닿아 있는지 여부를 확인할 수 있는 API가 추가되었습니다.
- isGround()가 true일 때만 점프 기능이 동작합니다.
```javascript
var camera = Module.getViewCamera();
camera.isGround();
```

#### 5. 착지 고도 설정 API 추가
- 플레이어 모드에서 카메라의 착지 고도를 직접 지정할 수 있는 기능이 추가되었습니다.
- 특정 고도를 수동으로 설정하거나, 현재 위치의 지형 고도를 자동으로 적용할 수 있습니다.
```javascript
var camera = Module.getViewCamera();
camera.setLandingElevation(50.0); // 특정 고도를 착지 고도로 설정
camera.setLandingElevationToTerrain(); // 지형 고도를 착지 고도로 설정
```

#### 6. 카메라 범위 외 레이어 피킹 API 추가
- 기존에는 카메라 시야 영역 내 객체만 피킹이 가능했지만, 시야 영역에 관계없이 피킹이 가능한 API가 추가되었습니다.
```javascript
let buildingLayer = Module.getTileLayerList().nameAtLayer("facility_build");
pickPosition = buildingLayer.getPickInfoAtView(_from, _to); // 기존: 카메라 영역 내부만 피킹
pickPosition = buildingLayer.getPickInfo(_from, _to); // 추가: 카메라 영역 상관 없이 피킹
```

#### 7. 영역 내부의 건물 오브젝트 아이디 반환 API 추가
- 영역 내부의 건물 오브젝트 아이디를 반환하는 API가 추가되었습니다.
```javascript
var boundary = [
  [126.93790903169547, 37.522875202560655, 0.0],
  [126.92841620055285, 37.516978366894115, 0.0],
  [126.91894402430914, 37.52022975707285, 0.0]
] // 고도값 유무 상관 없음

var objects = Module.getTileLayerList().nameAtLayer("facility_build").getObjectsInBoundary(boundary);

console.log(objects.id);
```

#### 8. 3DTiles 요청 및 렌더링 최적화
- 3DTiles 요청시 SSE 기준 요청으로 변경
- 요청 순서 최적화
- 요청 수 관리로 브라우저 안정화

#### 9. 모바일 서비스 안정화

 -   일부 기기에서 POI 객체 선택시 오류 수정

#### 10. 선택된 객체 리스트 반환
- [선택된 객체 리스트 반환](https://sandbox.egiscloud.com/code/main.do?engine=latest_test&id=object_select_info)

#### 11. 빌보드 객체 지형 아래 랜더링 오류 수정
- 빌보드 객체가 지형 아래로 내려가거나 걸칠경우 랜더링 되지 않는 현상 수정

### 2.20.1 (2025/11/11)
#### 1. JSFlowPolygon 인덱스 기반 생성 기능 추가
  - JSFlowPolygon 생성 시 버텍스 및 삼각분할 된 인덱스 기반으로 생성할 수 있도록 API 기능이 추가되었습니다.
    ``` javascript
    var polygon = Module.createFlowPolygon("FLOW_POLYGON");
    ...
    var result = polygon.create({
        vertex: geometry,                       // Polygon shape
        index : indices,                          // Triangulated index
        normaltexture: GLOBAL_FLOW_NOISE_TEXTURE,       // River flow noise texture
    });
    ```

### 2.20.0 (2025/11/03)
#### 1. 성능 개선 및 내부 안정화 작업을 수행하였습니다.

### 2.19.0 (2025/10/13)
#### 1. 오버레이 기능 오류 수정 [(이슈 #513)](https://github.com/EgisCorp/XDWorld/issues/513)
  * 간헐적으로 검은색 이미지가 오버레이 되는 현상이 수정되었습니다.
  * 이미지 오버레이 투명값 옵션이 추가되었습니다.
 ```javascript
polygon.setOverlayObject({
	style : "polygon",
	coordinate : vertex,
	alpha : 0.6,           // 추가된 옵션
	image : _image
});
 ```
  * 건물 심플모드에 오버레이 적용되지 않는 현상 수정
  * 건물 외곽선 렌더링을 원하지 않을 경우 : Module.SetSimpleModeLineRender(false);
    <img width="969" height="690" alt="image" src="https://github.com/user-attachments/assets/d4d0761e-c7b2-437e-a3d5-6eedbf4965bf" />

#### 2. 라인객체 GLOW 효과 개선
  * 기존 GLOW 효과를 개선하였습니다.
    <img width="645" height="619" alt="image" src="https://github.com/user-attachments/assets/c4dde99b-8e5d-48d9-a5d9-19758722d2f3" />

#### 3. JSPolygon 편집 API 추가
  * 이동, 회전, 스케일
  * [샌드박스 샘플](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_edit)
```javascript
let polygon = Module.createPolygon("POLYGON");

// 이동
polygon.move(longitude, latitude, alttitude);

// 회전
polygon.setRotation(x, y, z);

// 스케일
polygon.setScale(x, y, z);
```

#### 4. JSObject3D 축의 끝점 좌표 반환 API 추가
  * 회전, 스케일 시 축을 생성하여 직관적으로 확인할 수 있도록 축의 끝점 좌표를 반환하는 API가 추가되었습니다.
  * 중심과 끝점으로 라인을 생성합니다.
  * [샌드박스 샘플](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_edit)
```javascript
// axis (x: 0, y: 1, z: 2)
let endpoint = getAxisEndpoint(axis, length);
```
#### 5. 카메라 이동 오류 수정 [(이슈 #514)](https://github.com/EgisCorp/XDWorld/issues/514)
 - 카메라 이동 후 간헐적으로 카메라 방향이 틀어지는 현상이 있어 수정되었습니다.
#### 6. 심플모드 건물에서 Hsv 옵션 [(이슈 #512)](https://github.com/EgisCorp/XDWorld/issues/512)
  * 건물 레이어가 심플모드인 경우에도 Hsv 옵션이 정상 동작하도록 수정되었습니다.

#### 7. 타일 레이어의 폴리곤 기반 요청 영역 지정
  * JSLayer의 setLimitBoundary API가 기존 사각 영역을 포함하여 폴리곤 영역도 수용하도록 변경되었습니다.
  * 건물의 중점이 폴리곤 영역에 포함되면 데이터를 로드합니다.
  * createXDServerLayer API에 boundaryLimit 옵션으로도 설정할 수 있습니다.
    ``` javascript
    Module.getTileLayerList().createXDServerLayer({
	  url : "https://xdworld.server.url",
	  servername : "XDServer",
	  name : "layer_name",
	  type : 9,
	  minLevel : 0,
	  maxLevel : 15,
	  boundaryLimit : [
		[126.93005255915998, 37.529214172573376, 0.0],
		[126.94102835336719, 37.52029412432422, 0.0],
		[126.93891529125652, 37.51798498831805, 0.0],
		[126.92841620055285, 37.516978366894115, 0.0],
		[126.92514862234246, 37.51770012779483, 0.0],
		[126.91756299430655, 37.521708873949606, 0.0],
	  ]
    });
    ```

#### 8. 지형 이미지 음영 마스킹 기능 추가
  * 경위도 최소, 최대 좌표로 지정한 영역 외 지형 이미지를 음영처리하는 옵션 API가 추가되었습니다. 
    ``` javascript
    Module.getTerrain().setImageMask({
        active : true,
        range : {
            min : [126.917562, 37.516978],
            max : [126.941028, 37.529214],
        },
        color : {a : 200, r : 0, g : 0, b : 0}
    });
    ```

#### 9. 지형 내장 이미지 사용 여부 설정 API 추가
  * 엔진 내 내장된 0레벨 지구본 이미지 사용 여부를 설정하는 옵션이 Module.initialize API에 추가되었습니다.
  * true로 설정하는 경우 내장된 이미지를 사용하며, false로 설정하는 경우 지정한 이미지 서버로 0레벨 이미지를 요청합니다.
  * 디폴트 값은 true 입니다.
    ``` javascript
    Module.initialize({
        container: document.getElementById("map"),
        terrain : {
            dem : {
                url : "...",
                name : "dem",
                servername : "XDServer",
            },
            image : {
                url : "...",
                name : "tile",
                servername : "XDServer",
                useBuiltInZeroImage : false    // false로 설정 시 지정한 서버로부터 0레벨 이미지 수신
            },						
        },
        ....
    }
    ```
    
### 2.18.0 (2025/09/01)
#### 1. 오브젝트 선택 시 외곽선 렌더링
  * JSReal3D, JSGhostSymbol, JSPolygon 오브젝트 선택 시 아래 이미지와 같이 외곽선이 함께 출력됩니다.
    <img width="1424" height="649" alt="Image" src="https://github.com/user-attachments/assets/f30d6dc7-bdaf-4eb2-aa36-839d289ba876" />
  * JSOption의 setRenderSelectSilhouette API를 활용하여 외곽선을 끄고 켤 수 있습니다.
    ``` javascript
    Module.getOption().setRenderSelectSilhouette(true);   // on
    Module.getOption().setRenderSelectSilhouette(false);  // off
    ```

#### 2. DEM 단독 렌더링
  * 지형 영상 없이 DEM 단독으로 렌더링이 가능하도록 개선되었습니다.

#### 3. 화면 중심 기반 마우스 틸트, 회전 옵션 [(이슈 509)](https://github.com/EgisCorp/XDWorld/issues/509)
  * 마우스로 화면 틸트, 회전 시 화면 중앙점을 중심으로 움직이도록 옵션이 추가되었습니다.
    ``` javascript
    Module.getControl().setMouseClickCenterMode(true);
    ```


### 2.17.1 (2025/08/21)
#### 1. 이미지 기반 오버레이 기능 구현 [(이슈 502)](https://github.com/EgisCorp/XDWorld/issues/502)
  * 기존 색상으로만 표현되던 오버레이 기능을 이미지 기반으로도 적용할 수 있도록 기능이 업데이트 되었습니다.
    ``` javascript
    var polygon = Module.createOverlayObject("POLYGON");		
    var color = new Module.JSColor(255, 255, 0);		
    polygon.setOverlayObject({
  	  style : "polygon",
  	  coordinate : vertex,
	  color : color,
	  image : {
		width : img.width,
		height : img.height,
		data : ctx.getImageData(0, 0, img.width, img.height).data,
	  }
    });
    ```

#### 2. 수인한도분석 결과값 추가
  * 각 격자에 시간대별 일조량 추가
    ```javascript
    [결과값]
    0 : {
    	analysisList: {
    		0 : {sunrise: true, time: 10},	// sunrise(일조인지 아닌지), time(일조 시간, 입력한 분석텀)
    		1 : {sunrise: true, time: 10},
    		.
    		.
    		.
    	}, 
    	color: {
    		A : 120,
    		R : 166,
    		G : 166,
    		B : 166
    	}, 
    	continuevalue: 50, 
    	id: 'grid_0', 
    	isanalysis: true,
    	position : {
    		alt: 3.981043982319534,
    		lat: 35.1712107372302,
    		lon: 129.13061351968938
    	},
    	totalvalue : 500
    }
    .
    .
    .
    ```

#### 3. 하드웨어 가속 옵션 삭제
  * 하드웨어 가속 옵션 UI 삭제 및 console 경고 안내

#### 4. AABB 추가
  * ECEF 좌표계에서의 AABB 좌표를 반환하는 기능이 추가되었습니다.
    ``` javascript
    var box = _polygon.getBoundary();
    // AABB Coordinates to Spherical Coordinates
    // bottom(4), top(4)
    var boxArray = box.getBox();
    
    const corners = {
    	bottom: [
    		[boxArray.get(0).longitude, boxArray.get(0).latitude, boxArray.get(0).altitude],
    		[boxArray.get(1).longitude, boxArray.get(1).latitude, boxArray.get(1).altitude],
    		[boxArray.get(2).longitude, boxArray.get(2).latitude, boxArray.get(2).altitude],
    		[boxArray.get(3).longitude, boxArray.get(3).latitude, boxArray.get(3).altitude],
    	],
    	top: [
    		[boxArray.get(4).longitude, boxArray.get(4).latitude, boxArray.get(4).altitude],
    		[boxArray.get(5).longitude, boxArray.get(5).latitude, boxArray.get(5).altitude],
    		[boxArray.get(6).longitude, boxArray.get(6).latitude, boxArray.get(6).altitude],
    		[boxArray.get(7).longitude, boxArray.get(7).latitude, boxArray.get(7).altitude],
    	]
    };
    ```

### 2.17.0 (2025/08/11)
#### 1. Figure 객체 편집 UI 제어 API 추가
  - scaleLock, rotateLock, moveLock
    ```javascript
    let fig = Module.createFigure("figs");
    
    // 크기 UI 삭제
    fig.scaleUI = false;
    
    // 회전 UI 삭제
    fig.rotateUI = false;
    
    // 이동 UI 삭제
    fig.moveUI = false;
    ```

#### 2. 하드웨어 가속 옵션 안내
  - Chrome 브라우저가 아닐 경우 Chrome 브라우저 권장 안내
    
    <img width="436" height="124" alt="image" src="https://github.com/user-attachments/assets/4f0f740c-4d97-44c1-a4f3-e8f9b00bbf2b" />


  - Chrome 브라우저의 "하드웨어 가속" or "그래픽 가속" 을 사용하지 않을 경우 안내
    
    <img width="497" height="283" alt="image" src="https://github.com/user-attachments/assets/56b44112-ee37-4ae9-b722-0164d397ed14" />


#### 3. Indicator 기능 개선
 * 타겟이 카메라 뒤에 있는 경우 Indicator가 정상적으로 계산되지 않는 현상을 수정하였습니다.


### 2.16.1 (2025/07/15)
#### 1. 고용량 3DS 로딩 최적화 기능이 추가되었습니다.

```javascript
var polygon = Module.createPolygon("POLYGON_3DS_LOAD");
	polygon.loadFile({
		url : _strURL,
		align : "center",
		position : pos,
		rotate :  fAngle,
		rebuild : true,
		discardVertexData : true,   // 추가 : 좌표 GPU 업데이트 후 삭제
		compressObject : false,     // 추가 : Import 후 압축 vertex 압축 안함.
	});
```
#### 2. 건물 높이 기준 횡단면 선분 추출 기능 추가
   * 지정한 건물의 높이기준 외곽선분 추출 기능이 추가되었습니다.
   * object JSReal3D::getFloorSliceEdge(double _height) 
   * 반환값 예시
 ``` {
 {
    "header": {
        // 데이터 바운더리 최소, 최대 경위도
        "minLon": 126.927487351387,    
        "minLat": 37.52418520251252,
        "maxLon": 126.92795509699533,
        "maxLat": 37.52453873807533,
        // 설정한 단면 분석 높이
        "cutHeight": 12.5,
        // 설정한 건물의 중심점
        "location": {
            "lon": 126.92774196141701,
            "lat": 37.52434050186833,
            "alt": 39.250494956970215
        },
        // 건물의 최소, 최대 높이 (해발고도)
        "elevation": {
            "min": 12.125300407409668,
            "max": 66.37568950653076
        }
    },
    // 단면 선분 정보 [A점(경도,위도,높이)B점(경도,위도,높이)] [...] 
    "edge": [
        [
            126.9277111803299,
            37.52448908205179,
            22.275913742370903,
            126.927487351387,
            37.52435413856168,
            22.275933586061
        ],
        [
            126.9277111803299,
            37.52448908206028,
            22.27591446880251,
            126.92779354446381,
            37.524538738067506,
            22.27593025751412
        ],
       [ 
           ...
        ]
    ]
}
```


### 2.16.0 (2025/07/07)
#### 1. Camera 이동 관련 API 오류 수정
  * [카메라 이동](https://sandbox.egiscloud.com/code/main.do?id=camera_set_viewrect)
  * 카메라 이동시 설정된 위치가 아닌 다른 위치로 이동되는 오류가 있어 수정되었습니다.

#### 2. POI ahead 옵션 오류 수정
  * [Object ahead](https://sandbox.egiscloud.com/code/main.do?id=object_ahead)
  * POI ahead 옵션이 동작하지 않아 수정되었습니다.

#### 3. Tile Layer 요청 제한 기능 개선
  * [Request Limit](https://sandbox.egiscloud.com/code/main.do?id=layer_request_boundary)
  * 모든 객체가 load 된 이후에 요청 제한 기능이 실행되어 즉각적으로 반영되도록 기능 개선하였습니다.

#### 4. JSPolygon.createTMCoordPlane API 오류 수정
  * 특정 유형 데이터에서 격자 밀림현상이 수정되었습니다.

### 2.15.1 (2025/06/25)
#### 1. 바람 효과 표현중 2D 표현이 되지 않는 오류 수정
  * [관련 샌드박스](https://sandbox.egiscloud.com/code/main.do?id=effect_wind) 에서 Wind 2D 생성되지 않는 오류 수정 

### 2.15.0 (2025/06/02)

#### 1. 거리 측정 기능 오류 수정
  * 거리측정 데이터 삭제 후 재측정 시 라인이 생성되지 않는 현상을 수정하였습니다.

### 2.14.2 (2025/05/27)

#### 1. 고스트심볼에 조망보기, 가시권분석3D 개선
  * 고스트심볼에서 조망보기, 가시권분석(3D) 성능을 향상하였습니다.

#### 2. 카메라 이동 오류 수정 ([issue #495](https://github.com/EgisCorp/XDWorld/issues/495))
  * 같은 위치로 이동할 경우 오류가 발생하여 예외처리를 추가하였습니다.

#### 3. 객체가 지형 밑인지 위인지 사용자가 설정하는 함수
  * 객체가 지형 위, 아래인지에 따라서 투명값 렌더링 순서에 영향이 있어 애매한 객체는 사용자가 직접 지정 가능합니다.(ex : 지하도)
  * JSPolygon::setUnderground(boolean _bUnderground) : 지형 위 아래 설정
  * JSPolygon::getUnderground() : 지정 상태 반환
   ```javascript
        var LayerList = new Module.JSLayerList(true);
        var layer = LayerList.nameAtLayer("Layer");
        if(layer!=null)
        {
                var pObject = layer.keyAtObject("Object");
                if(pObject==null) return;
                       pObject.setUnderground(true);
        }
   ```

#### 4. 거리측정 기능 개선
  * 거리 측정 시 라인 지형결합 on/off 설정 API 추가하였습니다.
     * void setMeasureDistancePointUnionTerrain(bool _set);
       * 이후에 입력되는 라인의 지형결합 적용 여부를 설정할 수 있습니다.
       * Class : JSOption
       * Parameter
         * _set : 지형결합 적용 여부(true/false)
       * 예시
          ``` javascript
          Module.getOption().setMeasureDistancePointUnionTerrain(false);
          ```

#### 5. POI에 가까이 다가가는 경우 사라지는 현상 개선
  * JSLayer의 minDistance 값보다 큰 거리에서 POI가 사라지는 현상을 수정하였습니다.


### 2.14.1 (2025/05/19)

#### 1. JSLayer에 setAlpha API의 동작 방식 변경
  * 기존 Object의 속성을 일괄적 조회후 수정 방식에서 실시간 적용 방식으로 변경
  * 슬라이드 방식으로 투명도 처리 가능

#### 2. JSEditTerrain 개별 삭제 기능 추가 ([issue #492](https://github.com/EgisCorp/XDWorld/issues/492))
  * 성절토 List index로 삭제할 수 있는 기능 추가

#### 3. 좌표변환 추가 ([issue #494](https://github.com/EgisCorp/XDWorld/issues/494))
  * 기존 WMS의 지원 좌표계는 5개(4326, 5174, 5179, 5180, 5186)
  * EPSG:3765 좌표변환 추가
  * 다른 EPSG 좌표계 지원할 수 있도록 추가

#### 4. moveLonLatBoundarybyJson API 오류 수정 ([issue #495](https://github.com/EgisCorp/XDWorld/issues/495))
  * 이동 후 똑같은 위치로 다시 이동시 오류 발생하여 예외처리

#### 5. 이미지 오버레이 기능 오류 수정 ([issue #496](https://github.com/EgisCorp/XDWorld/issues/496))
  * 이미지 오버레이시 지형 결합되지 않는 오류 수정


### 2.14.0 (2025/05/12)

#### 1. JSCamera의 moveOvalDist 이동 기준 해제 ([issue #488](https://github.com/EgisCorp/XDWorld/issues/488))
  * API 실행 시 이동 여부 기준 100m를 해제하였습니다.
#### 2. 경사향 가시화 결과 갱신 오류 수정 ([issue #488](https://github.com/EgisCorp/XDWorld/issues/490))
  * 경사향 가시화 결과가 갱신되지 않는 현상을 수정하였습니다.
#### 3. 태풍 위험반경 표시 오류 수정
  * RTT 기반 태풍 위험반경이 표시되지 않는 현상을 수정하였습니다.
#### 4. JSHTMLObject 스테레오뷰 오류 수정 ([issue #491](https://github.com/EgisCorp/XDWorld/issues/491))
  * JSHTMLObject 스테레오뷰 실행시 위치 오류를 수정하였습니다.

### 2.13.0 (2025/04/07)

#### 1. 터파기 가시화 오브젝트 추가(https://github.com/EgisCorp/XDWorld/issues/476)
     * 기존 JSColorPipe 뿐만 아니라 JSFlowPolygon, JSPolygon, JSReal3d(건물) 오브젝트도 원형 터파기 영역에 보이도록 기능을 추가하였습니다.
     * 보이고자 하는 JSLayer의 setViewInTransparency API를 통해 보이기 여부를 설정할 수 있습니다.
     * 기본 값은 보이지 않음(false) 이며, JSColorPipe 객체는 예외적으로 보임 상태를 유지합니다.
     * void setViewInTransparency(bool _set)
       * Class : JSLayer
       * Parameter
         * _set(bool) : 보이기 여부(true 보임 / false 보이지 않음)
       ``` javascript
       layer.setViewInTransparency(true);
       ```
     * bool getViewInTransparency();
       * Class : JSLayer
       * Return
         * 보임 설정 여부(bool)
       ``` javascript
       var visible = layer.getViewInTransparency();
       ```

#### 2. JSPolygon의 Union mode 오류 수정 (https://github.com/EgisCorp/XDWorld/issues/478)
    - JSPolygon에 Union mode 설정 후 RTT 적용이 되지 않는 점을 수정하였습니다.

#### 3. 라인 효과 추가 및 정리
     - 라인 타입에 따른 옵션 및 매개변수 구조를 보다 사용하기 쉽도록 수정하였습니다.
     - 변경 사항
       - type: 기존 숫자로 입력하는 방식에서 Module.BLING (type: NORMAL, OUTLINE, GLOW, ARROW, DASH, FIRE, BLING, WARNING)등의 상수로 정의하도록 변경되었습니다.
       - animation, loopcount 속성을 추가하여 가시화 효과(type)에 따라 애니메이션 효과가 적용되도록 변경되었습니다.
     - 라인 크기를 고정시키는 옵션을 추가하였습니다.
     ```javascript
     [기존방식]
     let data = {
       coordinates: coordinates,
       type: 0,						// Solid line creation
       union: false,						// Terrain union status
       depth: true,						// Object overlap status
       color: new Module.JSColor(255, 255, 0, 0),		// ARGB
       width: 1,						// Line width
     };

     [변경된 방식]
     let data = {
       coordinates: coordinates,
       type: Module.BLING,					// Solid line creation
       union: false,						// Terrain union status
       depth: true,						// Object overlap status
       color: new Module.JSColor(255, 255, 0, 0),		// ARGB
       width: 1,						// Line width
       animation: true,					// Animation
       sizefix: true,						// size fixed
       loopcount: 1						// Animation loop count
     };
     ```

#### 4. POI 가시화 오류 수정

     - 카메라 영역을 벗어날 경우, POI가 화면에서 사라지는 오류를 수정하였습니다.
     - 이제부터 영역을 벗어나면 POI 높이를 조절하여 화면 내부에서 볼 수 있도록 변경됩니다.

#### 5. 빌보드 회전 타입 추가
     * 아래 이미지와 같이 지면과 수평한 빌보드의 회전 타입이 추가되었습니다.
       ![Image](https://github.com/user-attachments/assets/4002a632-4efe-4ba7-8bec-9382c1402d48)
     * JSBillboard의 setRotationMode API를 통해 mode 2번을 선택하시면 적용하실 수 있습니다.
       ``` javascript
       billboard.setRotationMode(2);
       ```

#### 6. 마우스 조작 이벤트 버튼 설정 기능 추가
     * 마우스 버튼을 통해 지도 조작(이동, 회전, 줌) 동작에 사용할 버튼을 설정할 수 있도록 하는 기능이 추가되었습니다.  
     * `setMouseControlEvent`를 통해 조작 타입별 버튼을 설정할 수 있으며, `getMouseControlEvent`로 현재 설정된 버튼 값을 조회할 수 있습니다.  
     * 조작 타입은 `"translate"`, `"rotate"`, `"zoom"` 중 하나이며, 버튼 값은 0(좌클릭), 1(휠클릭), 2(우클릭) 중 하나입니다.  
     * `bool setMouseControlEvent(string type, int button)`  
       * Class : JSControl  
       * Parameter  
         * `type` (string) : 조작 타입 ("translate", "rotate", "zoom")  
         * `button` (int) : 마우스 버튼 값 (0: 좌클릭, 1: 휠클릭, 2: 우클릭)  
       * Return  
         * 설정 성공 여부 (bool)  
       ```javascript
       JSControl.setMouseControlEvent("rotate", 2);  // 회전을 우클릭으로 설정
       ```
     * `int getMouseControlEvent(string type)`  
       * Class : JSControl  
       * Parameter  
         * `type` (string) : 조작 타입 ("translate", "rotate", "zoom")  
       * Return  
         * 해당 타입의 현재 마우스 버튼 값 (int)  
       ```javascript
       var zoomButton = JSControl.getMouseControlEvent("zoom");
       ```

### 2.12.3 (2025/03/17)
- XDServer의 POI 레이어 서비스에서 데이터 처리중 발생하는 오류를 수정하였습니다.
  - 이슈 : https://github.com/EgisCorp/XDWorld/issues/475

### 2.12.2 (2025/03/12)
- JSOption::setMaxRequestQueueSize() API 추가
  - 데이터 요청 큐의 크기(기본값은 5)를 조절하는 setMaxRequestQueueSize()가 추가되었습니다.
    ```javascript
    Module.getOption().setMaxRequestQueueSize(20);
    ```
    - 매개변수: 변경할 요청 큐의 크기(number)
- 3D 서비스 모델 요청시 처리 성능이 향상되었습니다.

### 2.12.1 (2025/03/11)
- 이미지 레이어가 가시화되지 않는 오류를 수정하였습니다.

### 2.12.0 (2025/03/10)

#### 1. POI 선택시 Text 위치 오류 수정
    - POI 선택시 setTextMargin 이 Text 에 적용되지 않는 오류를 수정하였습니다.

#### 2. 화면분할(Streo View) 모드에서 좌우 객체를 인식할 수 있도록 기능을 수정하였습니다.

#### 3. Text 형태의 POI 선택 인식 및 선택 효과 추가
    - 기존 POI처럼 Text도 선택과 선택 색상(picking color) 적용이 가능하도록 수정하였습니다.

#### 4. 3DTiles B3DM 선택 오류를 수정하였습니다.

#### 5. `AutoMove` 모드에서 카메라 회전 옵션 `lock orientation` 추가
    - `AutoMove` 모드에서 카메라를 자유롭게 회전시킬 수 있도록, `lock orientation` 옵션이 추가되었습니다.
       - 활성화(기본값): 카메라가 항상 다음 경로의 위치를 바라봅니다.
       - 비활성화: 카메라를 1인칭 시점에서 회전시킬 수 있습니다(오른쪽 마우스 버튼 사용).
    - 사용 방법
        ```Javascript
        // AutoMove 설정
        Module.getViewCamera().setAnimationSpeed(1);
        Module.getViewCamera().startAutoMove();
        Module.XDRenderData();

        // 비활성화 함으로써, 카메라 자유롭게 이동 가능
        Module.getViewCamera().setLockOrientationAutoMove(false);
        ```
      - 자세한 사용 방법은 [샌드박스 샘플](https://sandbox.egiscloud.com/code/main.do?id=camera_move_path_visualize)을 확인해주시기 바랍니다.

#### 6. 서비스 레이어 범위 제한 옵션 `boundaryLimit` 추가
     - 서비스 레이어에서 오브젝트를 요청할 때, 요청하는 범위를 경도/위도로 제한할 수 있도록 `boundaryLimit` 옵션이 추가되었습니다.
       - 활성화: 기존 방식에서, 미리 지정해 놓은 범위에 포함되는 오브젝트만 호출합니다.
          - 활성화한 이후에도, `JSLayer::setLimitBoundary()` API를 사용하여 범위를 제한하여야 합니다.
       - 비활성화(기본값): 기존 방식과 동일하게 오브젝트를 호출합니다.
     - 사용 방법
        ```Javascript
          // 샌드박스에서 제공하는 
          let layer = Module.getTileLayerList().createXDServerLayer({
            url : "https://xdworld.vworld.kr",
            servername : "XDServer3d",
            name : "facility_build",
            type : 9,
            minLevel : 0,
            maxLevel : 15
          });

          // Json 형태의 매개변수로 범위 지정
          layer.setLimitBoundary({
            boundary: {
              min: [129.125, 35.161],		// Lower left
              max: [129.141, 35.168]		// Upper right
            }
          });

          layer.boundaryLimit = true;   // 옵션 활성화
        ```
       - 자세한 사용 방법은 [샌드박스 샘플](https://sandbox.egiscloud.com/code/main.do?id=layer_request_boundary)을 확인해주시기 바랍니다.

### 2.11.2 (2025/02/24)

- 3DTiles B3DM 피킹이 제대로 되지 않던 오류를 수정하였습니다.

### 2.11.1 (2025/02/17)

- 다울지도 네트워크 요청시 발생하는 오류가 수정되었습니다.

### 2.11.0 (2025/02/10)

#### 1. `3DTiles` 높이 오프셋 옵션 추가
     - `import3DTiles()`에 높이 오프셋(단위 m)를 설정할 수 있는 옵션 `offsetZ`가 추가되었습니다.
     - 자세한 사용법은 아래 예시를 확인해주시기 바랍니다.
       ```javascript
       var pLayerList = new Module.JSLayerList(true);
       if(pLayerList==null) return;

       var pLayer = pLayerList.nameAtLayer("Layer3DTiles");
       if(pLayer==null)
       {
         pLayer = pLayerList.createLayer("Layer3DTiles", Module.ELT_3DTILES);
       }
       pLayer.import3DTiles({
         url : _strURL,
         autoMove : true,
         offsetZ : _fOffsetZ,  // 높이 오프셋. 단위 m
       });
       ```

#### 2. 성절토 바닥/옆면 타일링 텍스쳐 설정 API 추가
     * 성절토 바닥 텍스쳐 설정 시 텍스쳐 반복 출력(타일링)이 가능하도록 API가 추가되었습니다.
     * API 설정 시 1.0보다 큰 값을 n값을 입력하면 설정한 텍스쳐가 n번 반복 출력됩니다.
     * API 호출 이후 생성되는 성절토 객체에 해당 값이 적용됩니다.
     * 성절토 바닥면 텍스쳐 설정
       * bool setBottomTextureTilingScale(float u, float v)
         * class : JSEditTerrain
         * parameter
           * u : 가로 반복 u 좌표
           * v : 세로 반복 v 좌표 
      * 성절토 옆면 텍스쳐 설정
        * bool setSlopeTextureTilingScale(float u, float v)
          * class : JSEditTerrain
          * parameter
            * u : 가로 반복 u 좌표
            * v : 세로 반복 v 좌표 
     ``` javascript
     Module.getEditTerrain().setBottomTextureTilingScale(10.0, 10.0);
     Module.getEditTerrain().setSlopeTextureTilingScale(10.0, 10.0);
     ```

#### 3. 비디오 객체 오류 수정
    * 초기화 시 계속적으로 Hls 네트워크 요청하는 오류가 수정되었습니다.
    * 뒷배경 on/off 기능이 추가되었습니다. [비디오 객체](https://sandbox.egiscloud.com/code/main.do?id=object_video_placement)

#### 4. `JSLayer::setObjectVisibleWithBoundary()` API 추가
   - 매개변수로 전달한 좌표를 벗어날 경우, 오브젝트를 그리지 않도록 설정하는 함수를 추가하였습니다.
   - 함수 정보
     - boolean setObjectVisibleWithBoundary(number minLon, number maxLon, number minLat, number maxLat)
     - class : JSLayer
     - parameter
       - minLon: 최소 경도
       - maxLon: 최대 경도
       - minLat : 최소 위도
       - maxLat : 최대 위도
     ```javascript
      // 레이어 및 오브젝트 생성
      sampleLayer.setObjectVisibleWithBoundary(129.5, 130, 35.16, 35.19);
     ```

### 2.10.2 (2025/01/21)

#### 1. `3DTiles` 포맷 처리 기능 안정화
   - `3DTiles` 파일 처리 속도를 개선하였습니다.
   - 로딩한 모델이 깜박이는 오류를 수정하였습니다.

#### 2. 성절토 바닥 타일링 텍스처 설정 API 추가
   - 성절토 바닥 텍스쳐 설정 시 텍스쳐 반복 출력(타일링)이 가능하도록 API가 추가되었습니다.
   - API 설정 시 1.0보다 큰 값을 n값을 입력하면 설정한 텍스쳐가 n번 반복 출력됩니다.
   - API 호출 이후 생성되는 성절토 객체에 해당 값이 적용됩니다.
   - bool setBottomTextureTilingScale(float u, float v)
     - class : JSEditTerrain
     - parameter
      - u : 가로 반복 u 좌표
      - v : 세로 반복 v 좌표
    ```javascript
      Module.getEditTerrain().setBottomTextureTilingScale(10.0, 10.0);
    ```

#### 3. `JSPolygon` 텍스처 오류 수정
   - `JSpolygon` 객체에 반투명한 텍스처가 제대로 적용되지 않는 오류를 수정하였습니다.

### 2.10.1 (2025/01/03)

#### 1. `createTMCoordPlane()` 기능 개선
    - `createTMCoordPlane()` API의 매개변수 정의 방식이 수정되었습니다. 자세한 사항은 아래 문서를 확인하여 주시기 바랍니다.
        - 변경된 양식
            ```Javascript
            JSPolygon.createTMCoordPlane({
                llcorner : {
                  coordCode : [좌표계코드, 필수],
                  x : [좌하단 X 좌표, 필수],
                  y : [좌하단 Y 좌표, 필수]
                },
                grid : {
                  col : [그리드 가로 총수, 필수],
                  row : [그리드 세로 총수, 필수],
                  cellSize : [그리드 셀의 가로 세로 크기, 필수],
                  ratioMode : [New 배율모드 사용 여부 0 - 기존 gab방식, 1 - 배율모드사용, 선택],
                  xSplit : [ New 가로 분할 배율, ratioMode  1일때 필수],
                  ySplit : [ New 세로 분할 배율, ratioMode  1일때 필수]
                }
              });
            ```
        - 사용 예시
            ```Javascript
            polygon.createTMCoordPlane({
              llcorner : {
                coordCode : 20,
                x : 216701.99445382116 ,
                y : 220328.8122727003
              },
              grid : {
                col : 644,
                row : 585,
                cellSize : 10,
                ratioMode : 1,
                xSplit : 10,
                ySplit : 10
              }
            });
            ```

### 2.10.0 (2024/12/27)

#### 1. `Stereo View` 모드의 로컬 레이어 오류 수정

-   `Stereo View` 모드에서 로컬 레이어를 사용할 경우, POI가 왼쪽 화면에만 그려지는 오류를 수정하였습니다.


### 2.9.2 (2024/12/16)

#### 1. `Real3D` 텍스처 요청 개수 제한 API 추가

-   `Real3D`에서 최대 텍스처 요청 개수를 제한할 수 있도록, `JSOption::setMaxRequestTextureQueueSize()` API가 추가되었습니다.

    | Name           | Type   | Description                                 |
    | -------------- | ------ | ------------------------------------------- |
    | maxTextureSize | number | <p>텍스처를 요청하는 최대 개수(1~20개).</p> |

    ```javascript
    Module.getOption().setMaxRequestTextureQueueSize(20); // 20개의 텍스쳐 요청
    ```

#### 2. `Real3D` 텍스처 레벨 고정 API 추가

-   `Real3D`에서 요청하는 텍스처 레벨을 고정할 수 있도록, `JSMap::fixedTextureLevel()` API가 추가되었습니다.

    | Name  | Type   | Description                       |
    | ----- | ------ | --------------------------------- |
    | level | number | <p>텍스처 요청하는 레벨(0~5).</p> |

    ```javascript
    Module.getMap().fixedTextureLevel(0); // 고정레벨 지정
    ```

### 2.9.1 (2024/12/06)

#### 1. glTF 모델의 회전 및 크기 조절 기능 추가

-   glTF 모델을 유연하게 사용할 수 있도록, 회전과 크기 조절 기능이 추가되었습니다.
-   회전의 경우 XYZ축을 기준으로 회전 각도를 조절할 수 있습니다.
    ```javascript
    var polygon = Module.createGLTF("GLTF_Object");
    polygon.loadFile({
        url: url,
        type: "glb",
        position: pos,
        rotate: [0, 90, 0], // XYZ 축 방향 회적 각도(Degree)
        scale: [1.0, 10.0, 1.0], // XYZ축 방향 스케일 변경. (1.0= 원래 크기)
        rebuild: true,
    });
    ```

#### 2. split view 하이브리드 가시화 기능 추가

-   하이브리드 모드가 `split view`에서도 정상적으로 보일 수 있도록 기능을 추가하였습니다.

#### 3. stereo view/split view 모드 오브젝트 렌더링 오류 수정

-   `stereo view/split view` 모드에서, 반투명한 상태의 오브젝트 출력이 제대로 되지 않는 오류를 수정하였습니다.

#### 4. JSPolygon::setHeightByType() API 추가

-   `type`에 따라 평면 폴리곤의 윗면을 생성하는 API를 추가하였습니다.

    | Name             | Type   | Description                                                                                                                               |
    | ---------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
    | heightOrAltitude | number | <p>버텍스에 적용할 높이 혹은 고도.</p><p>0일 경우: 높이로 사용.</p><p>1일 경우: 고도로 사용.</p>                                          |
    | type             | number | <p>윗면 생성 방식 설정.</p><p>0일 경우: 각 밑면 버텍스에서 height만큼 높인 윗면 생성.</p><p>1일 경우: 균일한 고도의 평평한 윗면 생성.</p> |

    ```javascript
    var polygon = Module.createPolygon("POLYGON");
    var vertex = new Module.JSVec3Array();
    var part = new Module.Collection();

    for (var i = 0; i < _vertex.length; i++) {
        for (var j = 0; j < _vertex[i].length; j++) {
            vertex.push(_vertex[i][j]);
        }
        part.add(_vertex[i].length);
    }
    polygon.setPartCoordinates(vertex, part);

    // Set as a polyhedron polygon with height
    // type == 0
    //polygon.setHeightByType(80, 0);
    // type == 1
    polygon.setHeightByType(120, 1);

    //...
    ```

### 2.9.0 (2024/11/29)

#### 1. Inspector 기능 항목 추가

-   기존 `Inspector` 기능에서, 지형 데이터(dem/image)를 요청하는 대기열의 크기를 확인할 수 있도록 수정하였습니다.
-   자세한 사용법은 [샌드박스 샘플](https://sandbox.egiscloud.com/code/main.do?id=option_inspector)을 참고해주시기 바랍니다.

### 2.8.4_hotfix (2024/11/22)

#### 1. 깜박임 오류 수정

-   특정한 상황에서, 지도가 제대로 그려지지 않고 깜박이는 오류를 수정하였습니다.

#### 2. 건물 simple mode 옵션 추가

-   그라데이션 모드(아래에서부터 위로 점점 밝아지는 음영 효과)가 추가 되었습니다.
-   Light 방향을 조절할 수 있는 옵션이 추가되었습니다.

#### 3. HTMLObject의 element 속성 추가

-   `HTMLObject.element` 프로퍼티가 추가되었습니다.
-   자세한 사용법은 [메뉴얼](https://egiscorp.gitbook.io/xdworld-webgl-manual/introduce-1/object/jshtmlobject#properties)을 참고해주시기 바랍니다.

### 2.8.3_hotfix (2024/11/15)

#### 1. JSPolygon.setWaterEffect() 오류 수정

-   `JSPolygon`에서 setWaterEffect()를 호출시, 검은 배경이 나타나는 오류를 수정하였습니다.

### 2.8.2_hotfix (2024/11/08)

#### 1. glTF 애니메이션 오류 수정

-   특정 glTF 모델의 애니메이션이 정상적으로 재생되지 않는 오류를 해결하였습니다.

#### 2. `JSLayer`에 `object_ahead` 속성 추가

-   레이어 차원에서 `object_ahead` 옵션을 관리할 수 있도록, `JSLayer`의 속성이 추가되었습니다.
-   사용법
    1. 먼저 해당 옵션을 사용하기 위해, `JSOption.object_ahead` 를 `true`로 설정하여야 합니다.
    2. `JSOption`와 `JSLayer`의 `object_ahead` 가 모두 `true`일 경우, 해당 레이어에 속한 3d point 오브젝트에 옵션이 적용됩니다.
    -   `JSOption`의 `object_ahead` 가 `true`여도 `JSLayer` 의 `object_ahead` 가 `false`이면 옵션이 적용되지 않습니다.
-   `object_ahead` 란?
    -   (카메라 기준)지형 및 시설물(건물)이 3d point 오브젝트보다 가까이 있을 경우, 오브젝트가 가려지도록 하는 옵션
    -   자세한 사용법은 [링크](https://sandbox.egiscloud.com/code/main.do?id=object_ahead)를 참고해주시기 바랍니다.
-   주의 사항
    -   `JSLayer.object_ahead` 속성은 `ELT_3DPOINT` 레이어에만 적용됩니다. 다른 속성의 레이어에서는 `JSOption.object_ahead`을 사용해주시기 바랍니다.

### 2.8.1_hotfix (2024/11/01)

#### 1. JSTraceTarget의 glTF 애니메이션 포맷 지원

-   JSTraceTarget에서 애니메이션이 포함된 glTF 포맷을 지원하도록 기능이 확장되었습니다.

#### 2. Real3DPack의 객체 버전 확장 적용

-   Real3DPack 레이어가 다양한 버전의 객체를 사용할 수 있도록 기능이 확장되었습니다.

### 2.8.0 (2024/10/25)

#### 1. 지형과 알파 값이 있는 객체 간의 렌더링 순서 정리

-   지형과 알파(투명) 값이 존재하는 객체들과의 가시화가 어색하지 않도록, 렌더링 순서를 변경하였습니다.

#### 2. 파이프 색상 변경 오류 수정

-   간소화 상태에서 파이프 색상 변경 시 색상 값이 정상적으로 적용되지 않는 현상을 수정하였습니다.

#### 3. 외부 폰트 기반 POI Text 이미지 생성시 발생하는 오류 수정

-   Text 이미지 생성이 정상적으로 작동되지 않는 현상을 수정하였습니다.

#### 4. 소형 시설물의 LOD Texture 미적용 오류 수정

-   카메라 거리에 따른 시설물 LOD 변경 기능이 동작되지 않는 현상을 수정하였습니다.

#### 5. JSPolygon::createVerticalGrid() API 추가

-   수직 평면 그리드 객체를 생성하는 API가 추가되었습니다.
-   파라미터: 레이어명, 좌하단, 우상단, 새로 개수, 가로 개수
-   자세한 사용법은 [링크](https://sandbox.egiscloud.com/code/main.do?id=object_vertical_grid)를 참고해주시기 바랍니다.

#### 6. JSFigure::getRectInfo() API 추가

-   생성된 `Figure` 객체에서 4개의 꼭지점을 반환합니다.
-   자세한 사용법은 [링크](https://sandbox.egiscloud.com/code/main.do?id=object_figure_coordinate)를 참고해주시기 바랍니다.

### 2.6.1 (2024/09/03)

#### 1. 배경지도 오류 수정

-   0레벨 로딩시 텍스쳐 깨지는 현상 발생하여 수정하였습니다.

### 2.6.0 (2024/08/30)

#### 1. 지형 쉐이더 컴파일 오류 처리 기능 추가

-   지형 쉐이더를 컴파일할 경우, 디바이스별로 쉐이더 컴파일 조건이 다르므로 실패하는 경우가 있습니다.
-   이를 방지하기 위해, 컴파일 실패시 조건 수정후 다시 컴파일하는 기능이 추가되었습니다.

#### 2. 멀티뷰(화면 분할) 모드 오류 수정

-   `멀티뷰 모드`에서 지형이 깜박이던 현상을 수정했습니다.

#### 3. 멀티뷰(화면 분할) 모드 레이어 가시화 기능 추가

-   `멀티뷰 모드`에서, `RTT/하이브리드` 레이어의 가시화를 제어할 수 있는 기능이 추가되었습니다.

#### 4. POI 가시화 개선

-   POI 레벨 범위(시작, 끝)에 따른 가시화 구조를 수정하였습니다.
-   `ETLT_USER_LAYER`를 통해 생성한 POI에 대한 `object_ahead` 옵션 설정에 따른 가시화 기능을 수정하였습니다.

#### 5. Base Map 기능에서, Bing Map(전체)/OSM(Terrain) 항목 서비스 종료

-   Base Map에서, Bing Map과 Open Street Map(terrain)에 대한 서비스를 종료하였습니다.
-   자세한 사항은 [링크](https://sandbox.egiscloud.com/code/main.do?id=layer_basemap)를 참고해주시기 바랍니다.

### 2.5.1 (2024/08/09)

#### 1. JSHTMLObject 이동 기능 추가

-   JSHTMLObject 내부 변수 "position"을 통해 현재 위치와, 변경 위치 설정하는 변수가 추가되었습니다.
    ```javascript
    // Get
    let position = htmlObject.position;
    // Set
    let position = new Module.JSVector3D(lon, lat, alt);
    htmlObject.position = position;
    ```
-   입력, 출력은 경위도 값이 기준입니다.

#### 2. POI 가시범위 API 기능 개선 확장

-   JSPoint에 개선된 가시범위 설정 API가 추가되었습니다.
    ```javascript
    // 가시 범위 설정 예시
    poi.setRange({
        enable: true, // 가시 범위 사용 여부 setVisibleRange의 bEnable 파라메터와 동일
        min: 1.0, // 가시 범위 최소 범위 setVisibleRange의 dMin 파라메터와 동일
        max: 1000.0, // 가시 범위 최대 범위 setVisibleRange의 dMax 파라메터와 동일
        textMin: 1.0, // 가시 범위 텍스트 최소 범위 min 과 같거나 커야함
        textMax: 300.0, // 가시 범위 텍스트 최대 범위 max 과 같거나 작아야함
    });
    ```
-   기존 POI 객체 표현범위 설정 (Icon 기준)에서 Text에 대한 추가 표현 범위를 설정합니다.

#### 3. JSPipe 흐름 화살표 기능 개선

-   평면 형태의 화살표를 3차원 입체 구조로 개선하였습니다.
-   일부 지역에서 화살표 생성 시 방향이 올바르게 정렬되지 않는 현상을 수정하였습니다.
-   파이프 지점 높낮이에 따라 화살표의 틸트 각도가 함께 적용되도록 수정하였습니다.

#### 4. face 데이터로 JSPolygon을 생성하는 'JSPolygon.createWithFaces()' API 추가

-   사용자가 정의한 face 데이터를 기반으로 JSPolygon을 생성하는 기능이 추가되었습니다.
-   사용자는 형식에 맞춘 JSON 데이터를 파라메터로 전달함으로써, JSPolygon을 생성할 수 있습니다.
-   자세한 사용법은 샌드박스 [링크](https://sandbox.egiscloud.com/code/main.do?id=object_faces_to_polygon)를 참고하시기 바랍니다.

```javascript
let parameter = {
	upVector: /*업벡터 좌표축*/,
	cullMode: /*버텍스 정의 방향*/,
	position: /*모델 중심 위치*/,
	moveOffset: /*위치 오프셋(세부 조정)*/,
	faceInfo: [
		{
			vertex: /*버텍스 위치*/,
			matrix: /*변환(4x4 행렬)*/,
			indexVertex: /*버텍스 인덱스*/,
			indexUV: /*텍스처 좌표 인덱스*/,
			uv: /*실제 텍스처 좌표*/,
			normal: /*노멀 벡터*/,
			color: /*색상*/
		}
	]
}
polygon.createWithFaces(parameter);
```

### 2.5.0 (2024/7/26)

#### 1. 웹 워커 기능 개선

-   기능 개선 및 파일 용량을 감소하여 기능 개선하였습니다.

#### 2. 도로 시설물 생성 기능 개선

-   도로 시설물 중 교량의 교각이 일정 높이 이하인 부분은 생성이 되지 않도록 예외처리 단계가 추가되었습니다.

#### 3. 빌보드 수직선 옵션 추가

-   빌보드 중심을 기준으로, 지면까지의 수직선을 생성 및 수정하는 API가 추가되었습니다.
    ```javascript
    parameter = {
        visible: true, // 가시화 여부(기본값: false)
        width: 10.0, // 수직선 두께(기본값: 1.0)
        color: JSColor(255, 15, 100, 200), // 수직선 색상(기본값: JSColor(255, 255, 255, 255))
        altitude: 30.0, // 수직선 끝점 고도(기본값: 0)
    };
    billboard.setVerticalLine(parameter);
    ```
-   성공적으로 생성/수정하였을 경우 true를 반환합니다.
-   API의 자세한 사용법은 샌드박스 [링크](https://sandbox.egiscloud.com/code/main.do?id=object_billboard_line)를 확인해주시기 바랍니다.

#### 4. 지형의 0레벨 지구본 위성영상 자체 포함

-   0레벨에 대한 지구본 위성영상을 자체 포함하도록 적용 되었습니다.
-   지도 서버에 연결이 정상적이 않아도 지구본은 기본적으로 구성됩니다.
-   0 레벨 요청을 실패하여 반복적 네트워크 요청을 처리하지 않습니다.
-   엔진의 파일용량이 소폭 증가합니다.

### 2.4.0 (2024/6/28)

#### 1. 화면 분할 시 잔상이 남는 현상 수정

-   지형 투명도 조절과 함께 화면 분할 기능 사용 시 분할 화면에 잔상이 남는 현상을 수정하였습니다.
-   화면 분할 기능 사용 시 레이어 배치 방향이 반대로 보이는 점을 확인하여 수정하였습니다.

#### 2. Camera Quake의 진동 오류 수정

-   Camera Quake(카메라 흔들림)기능에서, 진동 주기가 초단위로 적용되는 오류를 수정하였습니다.

#### 3. JSFlowPolygon 객체 색상 설정 오류 수정

-   create API 실행 전 color 속성 설정 시 값이 정상적으로 반영되지 않는 현상을 수정하였습니다.

#### 4. 전광판, 비디오 객체 기능 개선

-   사용자 편의성을 위해 객체 생성 이후의 기능들 엔진 내부에 삽입 및 속도개선되었습니다.
-   기존 비디오 텍스쳐 관련 기능은 2024년까지 지원합니다.
-   새로운 사용법은 [비디오텍스쳐](https://sandbox.egiscloud.com/code/main.do?id=object_video)를 참고하시기 바랍니다.

#### 5. WMS 로딩 방식 선택

-   사용자의 통신 환경과 WMS 및 하이브리드 상태에 따라 선택 가능하도록 API가 추가되었습니다.

```javascript
// Default : 0
//Module.getOption().setHybridRenderType(0);   // 기존과 동일
Module.getOption().setHybridRenderType(1); // 변경된 순서에 따라 바로 반영
```

#### 6. 장해물 판별 기능 추가

-   카메라와 JSPoint, JSHTMLObject 객체 사이에 장해물(지형, 시설물) 존재 시 가시화 유무를 설정하는 변수를 추가 하였습니다.

```javascript
Module.getOption().object_ahead = 0; 기존 방식(장해물 미판정)
Module.getOption().object_ahead = 1; 장해물에 따른 가시화 설정
```

#### 7. 카메라 좌/우 이동 API 추가

-   카메라 이동 함수 moveLeftRight가 추가되었습니다.
-   지정한 값 만큼 카메라가 좌/우 방향으로 이동합니다.

```javascript
Module.getViewCamera().moveLeftRight(0.01);
Module.getViewCamera().moveLeftRight(-0.01);
```

#### 8. 레이어 화면 분할 렌더링 기능 오류 수정

-   화면 분할 기능 사용 시 좌/우 방향이 반대로 적용되는 현상을 수정하였습니다.
-   화면 분할 후 특정 화면에서 화면의 잔상이 남는 현상을 수정하였습니다 [이슈 #401](https://github.com/EgisCorp/XDWorld/issues/401)

### 2.3.1 (2024/5/31)

#### 1. (중요)glTF 최적화(WebWorker)

-   glTF 포맷과 관련하여, WebWorker가 업데이트 되었습니다.
-   업데이트된 WebWorker 빌드 파일의 사용을 권장합니다.

#### 2. JSColorGrid3D 오브젝트 속성 반환 함수 추가

-   JSColorGrid3D 오브젝트의 속성 반환 함수가 추가되었습니다.
-   [getCellBox] 인덱스에 해당하는 셀의 박스 좌표 정보를 반환합니다.
    -   박스 좌표는 상단/하단, 좌/우, 위/아래로 구분되는 좌표 8개를 반환합니다.
    -   반환 되는 박스의 좌표 속성 값의 순서는 아래와 같습니다.
        -   0 : upLeftTop
        -   1 : upRightTop
        -   2 : upRightBottom
        -   3 : upLeftBottom
        -   4 : downLeftTop
        -   5 : downRightTop
        -   6 : downRightBottom
        -   7 : downLeftBottom
    ```javascript
    var cellBox = grid.getCellBox(20, 12);
    ```
-   [getCellHeight] 인덱스에 해당하는 셀의 높이 값을 반환합니다.
    ```javascript
    var height = grid.getCellHeight(20, 12);
    ```
-   [getCellWidthCount] 그리드의 가로 셀 수를 반환합니다.
    ```javascript
    var widthCellCount = grid.getCellWidthCount();
    ```
-   [getCellHeightCount] 그리드의 세로 셀 수를 반환합니다.
    ```javascript
    var heightCellCount = grid.getCellHeightCount();
    ```

### 2.3.0 (2024/5/24)

#### 1. JSColorGrid 오브젝트 반환 기능 추가

-   JSLayer의 오브젝트 반환 시 JSColorGrid 오브젝트도 반환 가능하도록 기능을 추가하였습니다.

#### 2. 수인한도분석 진행률 반환 기능 추가

-   CJSAnalysisGridShadow::prograss 분석 진행률을 반환하는 callback 함수를 추가하였습니다.

#### 3. 수인한도분석 배척격자 오류 수정

-   배척격자가 그림자를 생성하거나, 선택이 되지 않는 오류가 수정되었습니다.

#### 4. JSPolygon으로 고스트 심볼 생성하는 기능 추가

-   고스트 심볼을 생성할 때 외부에서 모델 파일을 입력해주는 대신, 미리 생성한 JSPolygon으로 정의가 가능하도록 `JSGhostSymbolMap.insert()`에 `polygon`인자를 추가하였습니다.
-   자세한 사용법은 [샌드박스 - Ghostsymbol(Polygon)](https://sandbox.egiscloud.com/code/main.do?id=object_polygon_to_ghost_symbol)을 참고해주시기 바랍니다.

### 2.2.2 (2024/5/3)

#### 1. WMS 오류 해결

-   WMS 기능을 사용할 때, 깜박거리는 현상이 수정되었습니다.
