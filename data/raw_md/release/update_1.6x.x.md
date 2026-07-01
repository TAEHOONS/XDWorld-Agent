# 1.6x 버전 업데이트

## 추가된 클래스

## 추가된 API

### 2024/04/22

-   bool setFaceTextureWrapU(number \_face_index, int \_wrap_type)
-   bool setFaceTextureWrapV(number \_face_index, int \_wrap_type)

## 변경된 API

## 샌드박스 업데이트 내역

-   [2024/03/29: altitude analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_altdistance).

## - 업데이트 내역 -

### beta 2.2.2 (2024/5/3)

#### 1. WMS 오류 해결

-   WMS 기능을 사용할 때, 깜박거리는 현상이 수정되었습니다.

### 1.61.0 (2024/4/26)

#### 1. 수인한도분석 상세분석 옵션 추가

-   '수인한도분석' 기능에서, 상세한 분석을 위한 `isdetail` 프로퍼티가 추가되었습니다.
    -   true: 그리드 영역에 햇빛이 들지 않는 영역이 있을 경우, 일조량 계산하지 않음.
    -   false:절반이상 햇빛이 들면 일조량 계산.

#### 2. HeatMap API에 가중치 매개변수 추가

-   기존 히트맵 정보를 입력하는 API의 매개변수에 `가중치`가 추가되었습니다.
-   addHeatMapEX(JSVector3D(경도, 위도, 가중치)) : JSMap 클래스
    ```javascript
    var pMap = Module.getMap();
    pMap.setTerrainEffect(9); // 히트맵 설정
    for (var i = 0; i < 4000; ++i) {
        pMap.addHeatMapEX(new Module.JSVector3D(124.0 + Math.random() * 8.0, 34.0 + Math.random() * 6.0, 1.0));
    }
    ```
-   addHeatMapsEX(JSVec3Array(경도, 위도, 가중치)) : JSMap 클래스

    ```javascript
    var pMap = Module.getMap();
    pMap.setTerrainEffect(9); // 히트맵 설정
    var vList = new Module.JSVec3Array();

    vList.push(new Module.JSVector3D(128.388791, 36.398409, 1.0));
    vList.push(new Module.JSVector3D(126.745337, 35.019302, 2.0));
    vList.push(new Module.JSVector3D(128.902455, 35.319581, 3.0));
    vList.push(new Module.JSVector3D(129.147955, 36.119326, 4.0));
    vList.push(new Module.JSVector3D(129.073899, 37.210022, 5.0));
    vList.push(new Module.JSVector3D(128.373239, 37.765977, 6.0));
    vList.push(new Module.JSVector3D(127.108525, 37.658713, 7.0));
    vList.push(new Module.JSVector3D(126.256902, 36.562545, 8.0));
    vList.push(new Module.JSVector3D(127.445746, 36.10847, 9.0));
    vList.push(new Module.JSVector3D(127.820355, 36.78923, 10.0));
    vList.push(new Module.JSVector3D(127.033226, 37.521304, 1.0));
    vList.push(new Module.JSVector3D(127.042107, 37.520151, 1.0));
    vList.push(new Module.JSVector3D(127.04462, 37.51416, 1.0));
    vList.push(new Module.JSVector3D(127.048812, 37.518277, 1.0));
    vList.push(new Module.JSVector3D(127.030439, 37.506783, 1.0));
    vList.push(new Module.JSVector3D(127.028751, 37.505695, 1.0));

    pMap.addHeatMapsEX(vList);
    pMap.setEffectDistance(2000000);
    ```

### 1.60.1 / beta 2.2.1 (2024/4/22)

#### 1. JSPolygon 텍스쳐 매핑 옵션 추가

-   JSPolygon의 Face에 텍스쳐 이미지 적용 시 타일 매핑 설정이 가능하도록 API가 추가되었습니다.
-   Clamp to Edge / Repeat / Mirrored Repeat 옵션이 설정 가능합니다.
-   각 옵션 값 상수를 Module 객체를 통해 적용하실 수 있습니다.

-   bool setFaceTextureWrapU(number \_face_index, int \_wrap_type)

    -   Face의 텍스쳐 u좌표(이미지 가로 x 좌표와 매칭)의 타일링 옵션을 설정하는 함수입니다.
    -   Class : JSPolygon
    -   Prarmeter
        -   \_face_index (number) : 적용하고자 하는 JSPolygon의 face index
        -   \_wrap_type (number) : 텍스쳐 타일링 타입(Clamp to Edge / Repeat / Mirrored Repeat)

-   bool setFaceTextureWrapV(number \_face_index, int \_wrap_type)
    -   Face의 텍스쳐 v좌표(이미지 가로 y 좌표와 매칭)의 타일링 옵션을 설정하는 함수입니다.
    -   Class : JSPolygon
    -   Parameter
        -   \_face_index (number) : 적용하고자 하는 JSPolygon의 face index
        -   \_wrap_type (number) : 텍스쳐 타일링 타입(Clamp to Edge / Repeat / Mirrored Repeat)

```javascript
function setPolygonTextureWrapType(_polygon, _face_index, _wrap_type) {
    if (polygon) {
        polygon.setFaceTextureWrapU(_face_index, _wrap_type);
        polygon.setFaceTextureWrapV(_face_index, _wrap_type);

        Module.XDRenderData();
    }
}
```

#### 2. 측량(Straight-Line Distance) 기능 수정

-   건물 위를 둘러싸는 직선이 삭제되었습니다.

#### 3. JSLayer에서 타일레이어의 타일로딩 완료 콜백 추가

-   JSLayer에서 타일레이어의 타일로딩 완료 이벤트 콜백 함수가 추가되었습니다.
-   XDServer를 통해서 서비스 받는 타일레이어 ( [Module.getTileLayerList()](https://egiscorp.gitbook.io/xdworld-webgl-manual/introduce-1/layer/jslayerlist#createxdserverlayer-option-jslayer) ) 대상으로 적용됩니다.
-   레이어 속 타일에 대한 로딩시 식별객체가 함께 로딩되는 타입들 ( TILE_LAYER_TYPE_POI, TILE_LAYER_TYPE_GHOST_SYMBOL, TILE_LAYER_TYPE_VECTOR_PIPE, TILE_LAYER_TYPE_REAL3D_PACK)은 **타일 로드 완료시 콜백이 발생**하며 TILE_LAYER_TYPE_REAL3D인 경우는 타일로드 후에 모델링 데이터를 로딩하기에 **각 개별 모델이 로딩시 콜백이 발생**합니다.
-   JSLayer::setTileLoadCallback( \_callbackFunc ) 으로 사용할 수 있습니다.

```
// 콜백 파라메터 구조
idx : number
idy : number
layerName : string
layerType :  number
level :  number
objectList :  array [ objectKey1 (string), objectKey2 (string), ... ]
```

```
// 테스트 샘플
let gLayer = null;   // 객체 추출을 위한 레이어 변수
function loadCallback(e)
{
	console.log(e);
	e.objectList.forEach((objkey) => {
		let obj = gLayer.keyAtObject(objkey);               // 키를 통한 레이어에서 객체 인터페이스 반환
		if(obj != null && obj.getObjectType() == 8) {   // Real3D 개체 타입 확인
			obj.setFillColor(false, new Module.JSColor(255, 64, 255, 64));   // 색상 변경
		}
	});
}
function loadFacility3D() {
	var layer = Module.getTileLayerList().createXDServerLayer({
		url : "https://xdworld.vworld.kr",
		servername : "XDServer3d",
		name : "facility_build",
		type : 9,
		minLevel : 0,
		maxLevel : 15
	});

	layer.setTileLoadCallback(loadCallback);  // 콜백 적용
	gLayer = layer;
}
```

### 1.60.0 / beta 2.2.0 (2024/3/29)

#### 1. 건물을 통과하여 직선거리를 분석하는 API 추가

-   시작점과 끝점의 높이/거리/(오브젝트를 통과하여)직선거리를 측정하는 <측량> 기능이 추가되었습니다.
-   `JSOption`에 해당 기능의 콜백 함수를 등록할 수 있는 `callBackAltDistance()` API가 추가되었습니다.
    -   [샌드박스 링크](https://sandbox.egiscloud.com/code/main.do?id=analysis_measure_altdistance)
-   마우스 모드에 `MML_ANALYS_ALTDISTANCE`가 추가되었습니다.
