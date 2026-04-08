---
description: 지도 생성 및 설정하기 위한 API 입니다.
---

# Module_API

> Module.initialize를 통해 기본 지도를 생성할 수 있습니다.
>
> Module을 통해 다른 Class를 생성 후 사용이 가능합니다.

{% hint style="info" %}
Function initialize에 추가된 worker 항목은 2024년 2월 1일부터 베타 버전 엔진에서 지원됩니다. 엔진과 함께 제공되는 'XDWorldWorker.js', 'XDWorldWorker.wasm'을 이용하여 엔진에 발생할 수 있는 부하를 분산하여 처리합니다.
{% endhint %}

```javascript
Module.initialize({
    container: document.querySelector("Container ID"),
    terrain: {
        dem: {
            url: "Terrain DEM data request URL",
            name: "Terrain DEM layer name",
            servername: "Request Server name",
        },
        image: {
            url: "Terrain image data request URL",
            name: "Terrain image layer name",
            servername: "Request Server name",
        },
        worker: {
            use: "Use of web worker",
            path: "Web worker file request URL",
            count: "Set the number of web workers to use",
        },
    },
    defaultKey: "Issued key",
});
```

## Function

### initialize(object) -> object

> 지도를 생성합니다.
>
> worker 항목 옵션을 통해 web worker 기능을 활성화 합니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type                                                                  | Description                         |
| ---------- | --------------------------------------------------------------------- | ----------------------------------- |
| container  | HTML Element                                                          | 3D 지도를 포함할 Container Element. |
| terrain    | [Module.CreateOptions](moduleapi.md#module.createterrainoptions)      | 지형 설정 정보.                     |
| worker     | [Module.CreateWorkerOptions](moduleapi.md#module.createworkeroptions) | web worker 설정 정보.               |
| defaultKey | string                                                                | Engine API 발급키.                  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보.

{% endtab %}
{% tab title="Template" %}

```javascript
// Use sandbox
Module.initialize({
    container: document.getElementById("map"),
    terrain: {
        dem: {
            url: "https://xdworld.vworld.kr",
            name: "dem",
            servername: "XDServer3d",
            encoding: true,
        },
        image: {
            url: "https://xdworld.vworld.kr",
            name: "tile_mo_HD",
            servername: "XDServer3d",
        },
    },
    worker: {
        use: true,
        path: "./worker/XDWorldWorker.js",
        count: 5,
    },
    defaultKey: "Issued key",
});
```

{% endtab %}
{% endtabs %}

### getVersion() → string

> 현재 엔진의 버전을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   엔진 버전

{% endtab %}
{% tab title="Template" %}

```javascript
let version = Module.getVersion();
```

{% endtab %}
{% endtabs %}

### createBarGraph(id) → [JSBarGraph](../object/jsbargraph.md)

> 2차원 막대 그래프 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSBarGraph](../object/jsbargraph.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createBarGraph("newBarGraph");
```

{% endtab %}
{% endtabs %}

### createBarGraph3D(id) → [JSBarGraph3D](../object/jsbargraph3d.md)

> 3차원 막대 그래프 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSBarGraph3D](../object/jsbargraph3d.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createBarGraph3D("newBarGraph3D");
```

{% endtab %}
{% endtabs %}

### createBillboard(id) → [JSBillboard](../object/jsbillboard.md)

> 빌보드 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| key  | string | 객체 고유 명칭. |

-   Return
    -   [JSBillboard](../object/jsbillboard.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createBillboard("newBillboard");
```

{% endtab %}
{% endtabs %}

### createGhostSymbol(id) → [JSGhostSymbol](../object/jsghostsymbol.md)

> 고스트 심볼 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSGhostSymbol](../object/jsghostsymbol.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let ghostSymbol = Module.createGhostSymbol("newGhostSymbol");
```

{% endtab %}
{% endtabs %}

### createLineString(id) → [JSLineString](../object/jslinestring.md)

> 선 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSLineString](../object/jslinestring.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createLineString("newPolyLine");
```

{% endtab %}
{% endtabs %}

### createMultiPoint(id) → [JSMultiPoint](../object/jsmultipoint.md)

> 멀티 포인트 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSMultiPoint](../object/jsmultipoint.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createMultiPoint("newMultiPoint");
```

{% endtab %}
{% endtabs %}

### createPipe(id) → [JSPipe](../object/jspipe.md)

> 3차원 파이프 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSPipe](../object/jspipe.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createPipe("newPipe");
```

{% endtab %}
{% endtabs %}

### createPoint(id) → [JSPoint](../object/jspoint.md)

> POI 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSPoint](../object/jspoint.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createPoint("newPoint");
```

{% endtab %}
{% endtabs %}

### createPointGraph(id) → [JSPointGraph](../object/jspointgraph.md)

> 3차원 포인트 그래프 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSPointGraph](../object/jspointgraph.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createPointGraph("newGraph");
```

{% endtab %}
{% endtabs %}

### createSurfaceGraph(id) → [JSSurfaceGraph](../object/jssurfacegraph.md)

> 3차원 그물형 격자 그래프 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSSurfaceGraph](../object/jssurfacegraph.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createSurfaceGraph("newBarGraph3D");
```

{% endtab %}
{% endtabs %}

### createHTMLObject(id) → [JSHTMLObject](../object/jshtmlobject.md)

> HTML 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| id   | string | 객체 고유 명칭. |

-   Return
    -   [JSHTMLObject](../object/jshtmlobject.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let object = Module.createHTMLObject("newHTML");
```

{% endtab %}
{% endtabs %}

### getAnalysis() → [JSAnalysis](../analysis/jsanalysis.md)

> 분석 기능을 실행하는 [JSAnalysis](../analysis/jsanalysis.md) 객체를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSAnalysis](../analysis/jsanalysis.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var analysis = Module.getAnalysis();
```

{% endtab %}
{% endtabs %}

### getGhostSymbolMap() → [JSGhostSymbolMap](../object/jsghostsymbolmap.md)

> 고스트 심볼을 관리하는 [JSGhostSymbolMap](../object/jsghostsymbolmap.md) 객체를 반환합니다.

{% tabs %}
{% tab title="Infomation" %}

-   Return
    -   [JSGhostSymbolMap](../object/jsghostsymbolmap.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let map = Module.getGhostSymbolMap();
```

{% endtab %}
{% endtabs %}

### ~~getNavigation() → JSNavigationControl~~

> ~~Creates and returns an API object for setting map navigation (compass).~~
>
> 미 사용 API

{% tabs %}
{% tab title="Infomation" %}

-   Return
    -   ~~JSNavigationControl: 반환 성공.~~
    -   ~~null: 반환 실패.~~

{% endtab %}
{% tab title="Template" %}

```javascript
let navigation = Module.getNavigation();
```

{% endtab %}
{% endtabs %}

### getMap() → [JSMap](../map/jsmap.md)

> 지도 기능을 호출하는 ([JSMap](../map/jsmap.md)) 객체를 반환합니다.

{% tabs %}
{% tab title="Infomation" %}

-   Return
    -   [JSMap](../map/jsmap.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

javascript
let map = Module.getMap();


{% endtab %}
{% endtabs %}

### getSlope() → [JSSlope](../analysis/jsslope.md)

> 경사 분석을 관리하는 [JSSlope](../analysis/jsslope.md) 객체를 반환합니다.

{% tabs %}
{% tab title="Infomation" %}

-   Return
    -   [JSSlope](../analysis/jsslope.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let slope = Module.getSlope();
```

{% endtab %}
{% endtabs %}

### getSymbol() → [JSSymbol](../object/jssymbol.md)

> 이미지 아이콘([JSIcon](../object/jsicon.md))을 관리하는 [JSSymbol](../object/jssymbol.md) 객체를 반환합니다.

{% tabs %}
{% tab title="Infomation" %}

-   Return
    -   [JSSymbol](../object/jssymbol.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let symbol = Module.getSymbol();
```

{% endtab %}
{% endtabs %}

### getTerrain() → [JSTerrain](../map/jsterrain.md)

> 지형 설정 API를 호출하는 [JSTerrain](../map/jsterrain.md) 객체를 반환합니다.

{% tabs %}
{% tab title="Infomation" %}

-   Return
    -   [JSTerrain](../map/jsterrain.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
let terrain = Module.getTerrain();
```

{% endtab %}
{% endtabs %}

### Resize(width, height)

> 3D 지도 화면의 크기를 변경하는 API 입니다.
>
> 설정이 없을 경우, canvas 크기를 기준으로 3D viewport를 설정합니다.
>
> container 설정 시 container 크기에 맞츄어 3D viewprot를 설정합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name   | Type   | Description |
| ------ | ------ | ----------- |
| width  | number | 화면 너비.  |
| height | number | 화면 높이.  |

{% endtab %}
{% tab title="Template" %}

```javascript
Module.Resize(400, 300);
```

{% endtab %}
{% endtabs %}

### ~~SetProxy(proxy)~~

> Sets the bypass proxy URL.
>
> 미 사용 API

{% tabs %}
{% tab title="Infomation" %}

| Name  | Type   | Description |
| ----- | ------ | ----------- |
| proxy | string | Proxy URL.  |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### SetSimpleMode(type)

> 시설물 가시화 심플 모드를 설정합니다.
>
> 시설물 심플 모드 설정 시 시설물 이미지가 있더라도 단순한 색상으로 객체를 가시화 합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name | Type    | Description                                                |
| ---- | ------- | ---------------------------------------------------------- |
| type | boolean | <p>true: 심플모드 활성화.<br>false: 심플모드 비활성화.</p> |

{% endtab %}

{% tab title="Template" %}

```javascript
Module.SetSimpleMode(0);
Module.SetSimpleMode(1);
```

{% endtab %}
{% endtabs %}

### XDClearInputPoint() → boolean

> 입력 점 리스트를 초기화합니다.

{% tabs %}
{% tab title="Infomation" %}

-   Return
    -   true: 초기화 성공.
    -   false : 초기화 실패.

{% endtab %}

{% tab title="Template" %}

```javascript
Module.XDClearInputPoint();
```

{% endtab %}
{% endtabs %}

### XDEMapCreateLayer(layerName, url, port, select, visible, userLayer, layerType, minLevel, maxLevel)

> XDServer 기반 타일 레이어를 추가합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name  | Type    | Description                                                      |
| ----- | ------- | ---------------------------------------------------------------- |
| layerName | string | <p>레이어 이름.<br>XDServer에서 서비스 되는 레이어 이름 적용.</p> |
| url | string | <p>XDServer 서비스 URL</p> |
| port | boolean | <p>포트 번호(현재 미사용).</p> |
| select | boolean | <p>레이어 오브젝트 선택 가능 여부.</p> |
| visible | boolean | <p>레이어 가시화 여부.</p> |
| userLayer | boolean | <p>XDServer 서비스 여부<br>true: 서비스하는 경우.<br>false: 서비스하지 않는 경우.</p> |
| layerType | number | <p>레이어 타입.</p> |
| minLevel | number | <p>레이어 타일 최소 레벨.</p> |
| maxLevel | number | <p>레이어 타일 최대 레벨.</p> |

{% endtab %}

{% tab title="Template" %}

```javascript
Module.XDEMapCreateLayer("facility_build", "server.url", 0, true, true, false, 9, 0, 15);
```

{% endtab %}
{% endtabs %}

### XDEPlanetRefresh()

> 지형,영상 서버 변경 후 화면의 재 갱신을 요청합니다.

{% tabs %}
{% tab title="Template" %}

```javascript
Module.XDEPlanetRefresh();
```

{% endtab %}
{% endtabs %}

### XDSetCamPositionLonLat(longitude, latitude, distance, angle) → boolean

> 경/위도 기준으로 카메라 위치를 설정합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name  | Type    | Description                                                      |
| ----- | ------- | ---------------------------------------------------------------- |
| longitude | number | <p>카메라 위치 좌표(경도).</p> |
| latitude | number | <p>카메라 위치 좌표(위도).</p> |
| distance | number | <p>카메라 위치 좌표(고도).</p> |
| angle | number | <p>카메라의 기울기(tilt).</p> |

-   Return
    -   true: 이동 성공.
    -   false: 이동 실패(초기화가 되지 않았을 경우).

{% endtab %}

{% tab title="Template" %}

```javascript
Module.XDSetCamPositionLonLat(129.128265, 35.171834, 500.0, 20);
```

{% endtab %}
{% endtabs %}

### XDIsMouseOverDiv(block)

> 지도 내 클릭 이벤트 사용 유무를 설정합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name  | Type    | Description                                                      |
| ----- | ------- | ---------------------------------------------------------------- |
| block | boolean | <p>true: 클릭 이벤트 비활성화.<br>false: 클릭 이벤트 활성화.</p> |

{% endtab %}

{% tab title="Template" %}

```javascript
Module.XDIsMouseOverDiv(false);
```

{% endtab %}
{% endtabs %}

### XDIsKeyOverDiv(block)

> 지도 내 키보드 이벤트 사용 유무를 설정합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name  | Type    | Description                                                      |
| ----- | ------- | ---------------------------------------------------------------- |
| block | boolean | <p>true: 키보드 이벤트 비활성화.<br>false: 키보드 이벤트 활성화.</p> |

{% endtab %}

{% tab title="Template" %}

```javascript
Module.XDIsKeyOverDiv(false);
```

{% endtab %}
{% endtabs %}

### XDRenderData()

> 화면의 재 갱신을 요청합니다.
>
> 이벤트가 없을 경우 화면을 유지합니다.
>
> 이벤트 없이 화면 갱신이 필요할 경우 사용 가능합니다.

{% tabs %}
{% tab title="Template" %}

```javascript
Module.XDRenderData();
```

{% endtab %}
{% endtabs %}

### XDSetMouseState(mode)

> 마우스 모드를 변경합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name | Type   | Description                                             |
| ---- | ------ | ------------------------------------------------------- |
| mode | number | [Mouse Type List](../etc/type-list.md#mouse-type-list). |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### XDSetLayerMoveZ(layername, alt)

> 드론 LOD 높이를 설정합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name 		 | Type   | Description                         |
| ---------- | ------ | ----------------------------------- |
| layername  | string | 드론 LOD 레이어 이름. 				|
| alt 		 | number | 드론 LOD 레이어 높이 설정. 			|

-   Return
    -   true: 높이 설정 성공.
    -   false: 높이 설정 실패.
    -   실패 조건
        -   엔진이 로드되지 않았을 경우.
        -   레이어가 없을 경우.
	
-   Sample
    -   [Sandbox_Layer Drone LOD](https://sandbox.egiscloud.com/code/main.do?id=layer_drone_lod)

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### GoogleMap() / OpenStreetMap() / ArcMap() / ~~MapBox()~~ / WMTS() / BingMap() / KakaoMap() / NaverMap() / XDLMap() / SKYMap() / DawulMap()

> 배경지도를 변경합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSImageryProvider](../layer/jsImageryProvider.md): 생성 성공.
    -   null: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
```

{% endtab %}
{% endtabs %}

### setInspector(mode)

> 엔진 모니터링 사용 여부를 설정합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name | Type   | Description                                             |
| ---- | ------ | ------------------------------------------------------- |
| mode | boolean | 엔진 모니터링 사용 여부 설정. |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getInspector() → object

> 엔진 모니터링 결과값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   FPS: 현재 FPS.
    -   Terrain: 지형 요청 URL.
    -   Satellite: 영상 요청 URL.
    -   LayerCount: 총 레이어 수.
    -   LayerName: 레이어 이름.
    -   RequestCount: 요청 수.
    -   SuccessCount: 요청 성공 수.
    -   TotalRequestTime: 총 요청 시간.
    -   MaxRequestTime: 최대 요청 시간.
    -   AvgRequestTime: 평균 요청 시간.
    -   RenderObjCount: 현재 랜더링 객체 수.
    -   MaxRenderTime: 최대 랜더링 시간.
    -   AvgRenderTime: 평균 랜더링 시간.
    -   Layer: 레이어 리스트.
    -   LayerType: 레이어 타입.
    -   ObjectCount: 객체 수.
    -   FaceCount: face 수.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### refreshInspector()

> 엔진 모니터링을 초기화 합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name | Type   | Description                                             |
| ---- | ------ | ------------------------------------------------------- |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getTileLayerList() → [CJSLayerList](../layer/jslayerlist.md)

> 타일 레이어 리스트를 반환합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name | Type   | Description                                             |
| ---- | ------ | ------------------------------------------------------- |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getObjectLayerList() → [CJSLayerList](../layer/jslayerlist.md)

> 옥트리 레이어 리스트를 반환합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name | Type   | Description                                             |
| ---- | ------ | ------------------------------------------------------- |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}


## Type Definitions

### Module.CreateTerrainOptions

| Name  | Type                                                                                | Description          |
| ----- | ----------------------------------------------------------------------------------- | -------------------- |
| dem   | [Module.CreateTerrainOptions.DEM](moduleapi.md#module.createterrainoptions.dem)     | 지형 고도 설정 정보. |
| image | [Module.CreateTerrainOptions.Image](moduleapi.md#module.createterrainoptions.image) | 지형 영상 설정 정보. |

### Module.CreateWorkerOptions

| Name  | Type    | Description           |
| ----- | ------- | --------------------- |
| use   | boolean | web worker 사용 유무. |
| path  | string  | web worker 요청 url.  |
| count | number  | web worker 사용 개수. |

### Module.CreateTerrainOptions.DEM

| Name       | Type    | Description                                                                                              |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------- |
| url        | string  | 지형 고도 요청 url.                                                                                      |
| name       | string  | 지형 고도 레이어 명칭.                                                                                   |
| servername | string  | 요청 서버 명칭.                                                                                          |
| encoding   | boolean | <p>지형 고도 암호화 유무 설정.<br>true: 암호화 된 지형 고도 데이터.<br>false: 일반 지형 고도 데이터.</p> |

### Module.CreateTerrainOptions.Image

| Name       | Type   | Description            |
| ---------- | ------ | ---------------------- |
| url        | string | 지형 영상 요청 url.    |
| name       | string | 지형 영상 레이어 명칭. |
| servername | string | 요청 서버 명칭.        |
