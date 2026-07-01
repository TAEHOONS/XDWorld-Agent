---
description: 지도 설정 및 제어하기 위한 API 입니다.
---

# JSMap

> Module.getMap() API를 생성합니다.

```javascript
var map = Module.getMap();
```

## Function

### addHeatMaps(coordinates)

> 히트맵 좌표 목록 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                              |
| ----------- | ------------------------------------- | ---------------------------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 히트맵 위치 좌표(경도, 위도, 고도) 목록. |

-   Sample
    -   function loadHeatmapPoint 참조.
    -   [Sandbox_Heatmap](https://sandbox.egiscloud.com/code/main.do?id=effect_heatmap)

{% endtab %}
{% tab title="Template" %}

```javascript
var layerList = new Module.JSLayerList(true);
var layer = layerList.createLayer("HEATMAP_POI", Module.ELT_3DPOINT);
layer.setMaxDistance(60000000.0);

var vList = new Module.JSVec3Array();
var positions = [
    [129.12628252638348, 35.174613788186335, -127.18464569468051],
    [129.1278597986113, 35.1730738804656, -127.16845162212849],
    [129.12691776723804, 35.17243834516552, -127.23446262534708],
    [129.12837451707335, 35.171954803028704, -127.18164411373436],
];

positions.forEach(function (item, idx) {
    vList.push(new Module.JSVector3D(item[0], item[1], 0));
});

Module.getMap().clearHeatMap();
Module.getMap().setTerrainEffect(9);
Module.getMap().setDistance(200);
Module.getMap().setWeight(1);
Module.getMap().addHeatMaps(vList);
Module.getMap().setEffectDistance(1500000);
```

{% endtab %}
{% endtabs %}

### addInputPoint(lon, lat) → number

> 사용자 입력 지점을 추가합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description               |
| ---- | ------ | ------------------------- |
| lon  | number | 경도 좌표 (degrees 단위). |
| lat  | number | 위도 좌표 (degrees 단위). |

-   Return
    -   number: 등록된 사용자 입력 지점 총 수.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getMap().addInputPoint(127.4347, 35.7016);
```

{% endtab %}
{% endtabs %}

### clearHeatMap()

> 히트맵을 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

-   Sample
    -   function loadHeatmapPoint 참조.
    -   [Sandbox_Heatmap](https://sandbox.egiscloud.com/code/main.do?id=effect_heatmap)

{% endtab %}
{% tab title="Template" %}

```javascript
var layerList = new Module.JSLayerList(true);
var layer = layerList.createLayer("HEATMAP_POI", Module.ELT_3DPOINT);
layer.setMaxDistance(60000000.0);

var vList = new Module.JSVec3Array();
var positions = [
    [129.12628252638348, 35.174613788186335, -127.18464569468051],
    [129.1278597986113, 35.1730738804656, -127.16845162212849],
    [129.12691776723804, 35.17243834516552, -127.23446262534708],
    [129.12837451707335, 35.171954803028704, -127.18164411373436],
];

positions.forEach(function (item, idx) {
    vList.push(new Module.JSVector3D(item[0], item[1], 0));
});

Module.getMap().clearHeatMap();
Module.getMap().setTerrainEffect(9);
Module.getMap().setDistance(200);
Module.getMap().setWeight(1);
Module.getMap().addHeatMaps(vList);
Module.getMap().setEffectDistance(1500000);
```

{% endtab %}
{% endtabs %}

### clearInputPoint()

> 사용자 입력 좌표 목록을 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

-   Sample
    -   function clearInputPoint 참조.
    -   [Sandbox_LineBuffering](https://sandbox.egiscloud.com/code/main.do?id=object_line_buffering)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getMap().clearInputPoint();
```

{% endtab %}
{% endtabs %}

### clearSelectObj()

> 지도 내 선택된 모든 오브젝트를 선택 해제 상태로 변환합니다.

{% tabs %}
{% tab title="Information" %}
{% endtab %}

{% tab title="Template" %}

```javascript
Module.getMap().clearSelectObj();
```

{% endtab %}
{% endtabs %}

### clearSnowfallArea()

> 적설 효과를 초기화 합니다.

{% tabs %}
{% tab title="Information" %}
{% endtab %}

{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.clearSnowfallArea();
```

{% endtab %}
{% endtabs %}

### getInputPointCount() → number

> 사용자 입력 좌표 목록 개수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   result >= 0 : 반환 성공.
    -   -1: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var API = {
    Module.getMap();
};
var nCount = API.JSMap.getInputPointCount();
```

{% endtab %}
{% endtabs %}

### getInputPointList() → [Collection](../core/collection.md)

> 사용자 입력 좌표(경도, 위도, 고도)를 모두 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [Collection](../core/collection.md): 반환 성공.
    -   null: 반환 실패.
-   Sample
    -   function createPipe 참조.
    -   [Sandbox_LineBuffering](https://sandbox.egiscloud.com/code/main.do?id=object_pipe)

{% endtab %}
{% tab title="Template" %}

```javascript
var inputPoints = Module.getMap().getInputPointList();
```

{% endtab %}
{% endtabs %}

### getInputPoints() → [JSVec3Array](../core/jsvec3array.md)

> 사용자 입력 좌표(경도, 위도, 고도)를 모두 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVec3Array](../core/jsvec3array.md): 반환 성공.
    -   null: 반환 실패.
-   Sample
    -   function createBufferPolygon 참조.
    -   [Sandbox_LineBuffering](https://sandbox.egiscloud.com/code/main.do?id=object_line_buffering)

{% endtab %}
{% tab title="Template" %}

```javascript
var line = Module.getMap().getInputPoints();
```

{% endtab %}
{% endtabs %}

### getTerrHeight(lon, lat) → number

> 입력 변수값(lon, lat)의 해발고도 기준 지형 높이값을 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| lon  | number | 경도.       |
| lat  | number | 위도.       |

-   Return
    -   result > 0: 반환 성공.
    -   0: 반환 실패
    -   실패 조건
        -   해당 지형 고도 데이터가 지도에 요청 되지 않는 경우.
        -   요청 지형 레벨이 낮은 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var height = Module.getMap().getTerrHeight(126.92836647767662, 37.52439503321471);
```

{% endtab %}
{% endtabs %}

### GetPointDistance(from, to, type) → number

> 입력 변수값(from, to) 두 지점의 실제 거리를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type                                | Description                                                                       |
| ---- | ----------------------------------- | --------------------------------------------------------------------------------- |
| from | [JSVector3D](../core/jsvector3d.md) | 시작 좌표 (경도, 위도, 고도)                                                      |
| to   | [JSVector3D](../core/jsvector3d.md) | 종료 좌표 (경도, 위도, 고도)                                                      |
| type | boolean                             | <p> 지형 결합 유무를 설정합니다.<br>true: 지형 결합 거리.<br>false: 직선 거리.<p> |

-   Return
    -   result > 0: 반환 성공.
    -   0: 반환 실패

{% endtab %}
{% tab title="Template" %}

```javascript
var distance = Module.getMap().GetPointDistance(new Module.JSVector3D(129.128265, 35.171834, 500.0), new Module.JSVector3D(129.118265, 35.161834, 500.0), false);
```

{% endtab %}
{% endtabs %}

### getLineBuffer(coordinates, distance) → [JSVec2Array](../core/jsvec2array.md)

> 입력 변수값(coordinates)을 기준으로 직선에 대한 buffer의 폴리곤 좌표 목록을 반환합니다.
>
> 입력 변수값(distance)를 기준으로 버퍼 영역을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                        |
| ----------- | ------------------------------------- | ---------------------------------- |
| coordinates | [JSVec2Array](../core/jsvec2array.md) | 선 좌표 목록 (경위도).             |
| distance    | number                                | buffer의 반지름 크기 (meter 단위). |

-   Return
    -   [JSVec2Array](../core/jsvec2array.md): 반환 성공.
    -   null: 반환 실패.
-   Sample
    -   function createBufferPolygon 참조.
    -   [Sandbox_LineBuffering](https://sandbox.egiscloud.com/code/main.do?id=object_line_buffering)

{% endtab %}
{% tab title="Template" %}

```javascript
var map = Module.getMap();
var line = map.getInputPoints();
var line2D = new Module.JSVec2Array();
for (var i = 0; i < line.count(); i++) {
    line2D.push(new Module.JSVector2D(line.get(i).Longitude, line.get(i).Latitude));
}
var polygonLine = map.getLineBuffer(line2D, 100);
```

{% endtab %}
{% endtabs %}

### MapRender()

> 3D 지도 화면을 재 갱신합니다.

{% tabs %}
{% tab title="Information" %}
{% endtab %}

{% tab title="Template" %}

```javascript
Module.getMap().MapRender();
```

{% endtab %}
{% endtabs %}

### MapToScreenPointEX(position) → [JSVector2D](../core/jsvector2d.md)

> 3D 지도에서 특정 지점에 대한 화면 좌표를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                        |
| -------- | ----------------------------------- | ---------------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 지도 위치 좌표 (경도, 위도, 고도). |

-   Return
    -   [JSVector2D](../core/jsvector2d.md): 반환 성공.
    -   null: 반환 실패.
-   Sample
    -   function displayPopUp 참조.
    -   [Sandbox_MapToScreenCoordinate](https://sandbox.egiscloud.com/code/main.do?id=coordinate_map_to_screen)

{% endtab %}
{% tab title="Template" %}

```javascript
var pointMapPos = Module.getMap().MapToScreenPointEX(new Module.JSVector3D(129.128265, 35.171834, 100.0));
```

{% endtab %}
{% endtabs %}

### ScreenToMapPointEX(position) → [JSVector3D](../core/jsvector3d.md)

> 화면 좌표에서 특정 지점에 대한 3D 지도 좌표를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description       |
| -------- | ----------------------------------- | ----------------- |
| position | [JSVector2D](../core/jsvector2d.md) | 화면 좌표 (x, y). |

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 반환 성공.
    -   null: 반환 실패.
-   Sample
    -   function init 참조.
    -   [Sandbox_ScreenToMapCoordinate](https://sandbox.egiscloud.com/code/main.do?id=coordinate_screen_to_map)

{% endtab %}
{% tab title="Template" %}

```javascript
var mapPosition = Module.getMap().ScreenToMapPointEX(10, 10);
```

{% endtab %}
{% endtabs %}

### setCircleInputPoint(center, radius, segment)

> 특정 지점에 대한 반경 좌표 목록을 반환합니다.
>
> 입력 변수값(center)을 기준으로 입력 변수값(radius)을 반지름으로 반경에 대한 좌표를 반환합니다.
>
> 입력 변수값(segment)으로 반경을 정밀도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type                                | Description                  |
| ------- | ----------------------------------- | ---------------------------- |
| center  | [JSVector2D](../core/jsvector2d.md) | 반경의 중심 좌표(경도 위도). |
| radius  | number                              | 반경의 반지름 (meters 단위). |
| segment | number                              | 반경의 정밀도.               |

{% endtab %}
{% tab title="Template" %}

```javascript
var vCenter = new Module.JSVector(129.1475, 35.184338);
Module.getMap().setCircleInputPoint(vCenter, 500.0, 12);
```

{% endtab %}
{% endtabs %}

### setDistance(distance)

> 히트맵 반경거리를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description       |
| -------- | ------ | ----------------- |
| distance | number | 히트맵 영역 거리. |

-   Sample
    -   function loadHeatmapPoint 참조.
    -   [Sandbox_Heatmap](https://sandbox.egiscloud.com/code/main.do?id=effect_heatmap)

{% endtab %}
{% tab title="Template" %}

```javascript
var layerList = new Module.JSLayerList(true);
var layer = layerList.createLayer("HEATMAP_POI", Module.ELT_3DPOINT);
layer.setMaxDistance(60000000.0);

var vList = new Module.JSVec3Array();
var positions = [
    [129.12628252638348, 35.174613788186335, -127.18464569468051],
    [129.1278597986113, 35.1730738804656, -127.16845162212849],
    [129.12691776723804, 35.17243834516552, -127.23446262534708],
    [129.12837451707335, 35.171954803028704, -127.18164411373436],
];

positions.forEach(function (item, idx) {
    vList.push(new Module.JSVector3D(item[0], item[1], 0));
});

Module.getMap().clearHeatMap();
Module.getMap().setTerrainEffect(9);
Module.getMap().setDistance(200);
Module.getMap().setWeight(1);
Module.getMap().addHeatMaps(vList);
Module.getMap().setEffectDistance(1500000);
```

{% endtab %}
{% endtabs %}

### setEffectDistance(max)

> 홍수, 적설, 히트맵 가시화 최대 거리를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description           |
| ---- | ------ | --------------------- |
| max  | number | 가시화 최대 가시거리. |

-   Sample
    -   function loadHeatmapPoint 참조.
    -   [Sandbox_Heatmap](https://sandbox.egiscloud.com/code/main.do?id=effect_heatmap)

{% endtab %}
{% tab title="Template" %}

```javascript
var layerList = new Module.JSLayerList(true);
var layer = layerList.createLayer("HEATMAP_POI", Module.ELT_3DPOINT);
layer.setMaxDistance(60000000.0);

var vList = new Module.JSVec3Array();
var positions = [
    [129.12628252638348, 35.174613788186335, -127.18464569468051],
    [129.1278597986113, 35.1730738804656, -127.16845162212849],
    [129.12691776723804, 35.17243834516552, -127.23446262534708],
    [129.12837451707335, 35.171954803028704, -127.18164411373436],
];

positions.forEach(function (item, idx) {
    vList.push(new Module.JSVector3D(item[0], item[1], 0));
});

Module.getMap().clearHeatMap();
Module.getMap().setTerrainEffect(9);
Module.getMap().setDistance(200);
Module.getMap().setWeight(1);
Module.getMap().addHeatMaps(vList);
Module.getMap().setEffectDistance(1500000);
```

{% endtab %}
{% endtabs %}

### setSnowfallArea(array)

> 적설 효과를 표현할 영역을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                                  | Description                        |
| ----- | ------------------------------------- | ---------------------------------- |
| array | [JSVec3Array](../core/jsvec3array.md) | 영역 좌표 목록 (경도, 위도, 고도). |

{% endtab %}

{% tab title="Template" %}

```javascript
var vAreaList = new Module.JSVec3Array();
vAreaList.push(new Module.JSVector3D(129.0952984771729, 35.26956608261821, 130.72385844029486));
vAreaList.push(new Module.JSVector3D(129.17153320599272, 35.26955240007246, 171.6742866402492));
vAreaList.push(new Module.JSVector3D(129.17146263440185, 35.17317375381265, 34.883301799185574));
vAreaList.push(new Module.JSVector3D(129.09531779839347, 35.17318816290076, 60.5584503589198));
vAreaList.push(new Module.JSVector3D(129.0952984771729, 35.26956608261821, 130.72385844029486));
Module.getMap().setSnowfallArea(vAreaList);
```

{% endtab %}
{% endtabs %}

### setSnowfallColor(color)

> 적설 효과에서 표현되는 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| color | [JSColor](../core/jscolor.md) | 적설 색상.  |

{% endtab %}

{% tab title="Template" %}

```javascript
var snowColor = new Module.JSColor(178, 178, 178);
Module.getMap().setSnowfallColor(snowColor);
```

{% endtab %}
{% endtabs %}

### setTerrLODRatio(ratio)

> 지형 LOD 요청 거리 비율을 설정합니다.
>
> 설정에 따라 먼거리에서 정밀한 지형 데이터가 가시화 됩니다.
>
> \<LOD에 따른 지형 갱신 거리\> = \ratio \* \<지형 메쉬 사이즈\>

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description     |
| ----- | ------ | --------------- |
| ratio | number | 갱신 거리 비율. |

{% endtab %}

{% tab title="Template" %}

```javascript
Module.getMap().setTerrLODRatio(1.0);
```

{% endtab %}
{% endtabs %}

### setWeight(weight)

> 히트맵 가중치를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description    |
| ------ | ------ | -------------- |
| weight | number | 히트맵 가중치. |

-   Sample
    -   function loadHeatmapPoint 참조.
    -   [Sandbox_Heatmap](https://sandbox.egiscloud.com/code/main.do?id=effect_heatmap)

{% endtab %}
{% tab title="Template" %}

```javascript
var layerList = new Module.JSLayerList(true);
var layer = layerList.createLayer("HEATMAP_POI", Module.ELT_3DPOINT);
layer.setMaxDistance(60000000.0);

var vList = new Module.JSVec3Array();
var positions = [
    [129.12628252638348, 35.174613788186335, -127.18464569468051],
    [129.1278597986113, 35.1730738804656, -127.16845162212849],
    [129.12691776723804, 35.17243834516552, -127.23446262534708],
    [129.12837451707335, 35.171954803028704, -127.18164411373436],
];

positions.forEach(function (item, idx) {
    vList.push(new Module.JSVector3D(item[0], item[1], 0));
});

Module.getMap().clearHeatMap();
Module.getMap().setTerrainEffect(9);
Module.getMap().setDistance(200);
Module.getMap().setWeight(1);
Module.getMap().addHeatMaps(vList);
Module.getMap().setEffectDistance(1500000);
```

{% endtab %}
{% endtabs %}

### setFog(color, start, end, density)

> 안개 효과를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type                          | Description                     |
| ------- | ----------------------------- | ------------------------------- |
| color   | [JSColor](../core/jscolor.md) | 안개 색상.                      |
| start   | number                        | 가시화 최소 거리 (최소값 1).    |
| end     | number                        | 가시화 최대 거리.               |
| density | number                        | 안개 농도 (0.0 and 1.0 사이값). |

-   Sample
    -   function loadHeatmapPoint 참조.
    -   [Sandbox_Fog](https://sandbox.egiscloud.com/code/main.do?id=weather_fog)

{% endtab %}
{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.setFogLimitAltitude(6000000.0);
pMap.setFogEnable(true);
var color = new Module.JSColor(255, 255, 255, 255);
pMap.setFog(color, 0, 5000, 0.3);
```

{% endtab %}
{% endtabs %}

### setFogEnable(type)

> 안개효과 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                 |
| ---- | ------- | ----------------------------------------------------------- |
| type | boolean | <p>true: 안개 효과 가시화.<br>false: 안개 효과 비가시화</p> |

-   Sample
    -   function loadHeatmapPoint 참조.
    -   [Sandbox_Fog](https://sandbox.egiscloud.com/code/main.do?id=weather_fog)

{% endtab %}
{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.setFogLimitAltitude(6000000.0);
pMap.setFogEnable(true);
var color = new Module.JSColor(255, 255, 255, 255);
pMap.setFog(color, 0, 5000, 0.3);
```

{% endtab %}
{% endtabs %}

### setRainImageURL(url) → boolean

> 비 효과에 사용할 이미지를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| ---- | ------ | ------------ |
| url  | string | 이미지 경로. |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.

-   Sample
    -   function changeRainEffectOption 참조.
    -   [Sandbox_Rain](https://sandbox.egiscloud.com/code/main.do?id=weather_rain)

{% endtab %}
{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.setRainImageURL("./data/snow./png");
pMap.startWeather(1, 5, 5);
```

{% endtab %}
{% endtabs %}

### setSnowfall(state)

> 지형에 적설 효과적설 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                                                   |
| ----- | ------ | ------------------------------------------------------------- |
| state | number | <p>0: 지형 적설 효과 비가시화<br>1: 지형 적설 효과 가시화</p> |

-   Sample
    -   function setUseSnowEffect 참조.
    -   [Sandbox_Snow](https://sandbox.egiscloud.com/code/main.do?id=weather_snow)

{% endtab %}
{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.startWeather(0, 5, 5);
pMap.setSnowfall(1);
pMap.setSnowfallLevel(2.0);
```

{% endtab %}
{% endtabs %}

### setSnowfallLevel(level) → number

> 적설 교과 가시화 중 적설 적설량 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description           |
| ----- | ------ | --------------------- |
| level | number | 적설량(0~100 사이값). |

-   Return

    -   number: 설정된 적설량.

-   Sample
    -   function setUseSnowEffect 참조.
    -   [Sandbox_Snow](https://sandbox.egiscloud.com/code/main.do?id=weather_snow)

{% endtab %}
{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.startWeather(0, 5, 5);
pMap.setSnowfall(1);
pMap.setSnowfallLevel(2.0);
```

{% endtab %}
{% endtabs %}

### setSnowImageURL(url) → boolean

> 적설 효과 시 눈 이미지를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description          |
| ---- | ------ | -------------------- |
| url  | string | 눈 표현 이미지 경로. |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.

-   Sample
    -   function changeRainEffectOption 참조.
    -   [Sandbox_Snow](https://sandbox.egiscloud.com/code/main.do?id=weather_snow)

{% endtab %}
{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.setSnowImageURL("./data/snow./png");
pMap.startWeather(0, 5, 5);
pMap.setSnowfall(1);
pMap.setSnowfallLevel(2.0);
```

{% endtab %}
{% endtabs %}

### startWeather(type, size, speed) → boolean

> 날씨 효과 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                                 |
| ----- | ------ | ------------------------------------------- |
| type  | number | 날씨 유형(0: 눈, 1: 비).                    |
| size  | number | 날씨 강도 (0: 약함, 1: 보통, 2: 강항).      |
| speed | number | 날씨 표현 속도 (0: 느림, 1: 보통, 2: 빠름). |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.

-   Sample
    -   function setUseRainEffect 참조.
    -   [Sandbox_Rain](https://sandbox.egiscloud.com/code/main.do?id=weather_rain)

{% endtab %}
{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.startWeather(1, 5, 5);
```

{% endtab %}
{% endtabs %}

### stopWeather()

> 날씨 효과 기능을 비활성화 합니다.

{% tabs %}
{% tab title="Information" %}
{% endtab %}

{% tab title="Template" %}

```javascript
var pMap = Module.getMap();
pMap.stopWeather();
```

{% endtab %}
{% endtabs %}

### setSimpleMode(type) → boolean

> 시설물 색상 표현 심플 모드 설정합니다.
>
> 시설물 텍스쳐가 없는 색상으로 가시화 됩니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                                  |
| ---- | ------- | ------------------------------------------------------------ |
| type | boolean | <p>true: 심플 모드 활성화.<br>false: 심플 모드 비활성화.</p> |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.

-   Sample
    -   function setUseRainEffect 참조.
    -   [Sandbox_BuildingSimpleMode](https://sandbox.egiscloud.com/code/main.do?id=layer_building_simplemode)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getMap().setSimpleMode(true);
```

{% endtab %}
{% endtabs %}

### setTerrainEffect(value)

> 지형 가시화 효과를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description                                        |
| ----- | ------ | -------------------------------------------------- |
| value | number | 지형 가시화 효과 (0: 일반, 10: 경사향, 11: 경사도) |

-   Sample
    -   function setUseRainEffect 참조.
    -   [Sandbox_BuildingSimpleMode](https://sandbox.egiscloud.com/code/main.do?id=terrain_rendermode)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getMap().setTerrainEffect(10);
```

{% endtab %}
{% endtabs %}

### updateRTT()

> 3D 지도에 RTT 가시화를 재 갱신합니다.

{% tabs %}
{% tab title="Information" %}
{% endtab %}
{% tab title="Template" %}

```javascript
Module.getMap().updateRTT();
```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getSelectObject(), setSelectObject(object) → [JSObject](../object/jsobject.md)

> 객체의 선택 상태를 설정합니다.

{% tabs %}
{% tab title="Infomation" %}

| Name   | Type                              | Description  |
| ------ | --------------------------------- | ------------ |
| object | [JSObject](../object/jsobject.md) | 시설물 객체. |

-   Return
    -   [JSObject](../object/jsobject.md): 시설물 객체.

{% endtab %}
{% tab title="Template" %}

```javascript
var selObject = Module.getMap().getSelectObject();
// ... or ...
var object = GLOBAL.Layer.keyAtObject("object_select");
Module.getMap().setSelectObject(object);
```

{% endtab %}
{% endtabs %}

### getFogLimitAltitude(), setFogLimitAltitude(altitude) → number

> 안개 효과가 적용되는 영역에 대한 고도값을 설정합니다.
>
> 카메라가 반환 고도 아래에 있으면 안개효과가 적용됩니다.

{% tabs %}
{% tab title="Infomation" %}

| Name     | Type   | Description                  |
| -------- | ------ | ---------------------------- |
| altitude | number | 안개 효과 높이 (meter 단위). |

-   Return

    -   number: 안개 효과가 적용된 해발고도 기준 높이값.

-   Sample
    -   function loadHeatmapPoint 참조.
    -   [Sandbox_Fog](https://sandbox.egiscloud.com/code/main.do?id=weather_fog)

{% endtab %}
{% tab title="Template" %}

```javascript
var limitAltitude = Module.getMap().getFogLimitAltitude();
// ... or ...
var pMap = Module.getMap();
pMap.setFogLimitAltitude(6000000.0);
pMap.setFogEnable(true);
var color = new Module.JSColor(255, 255, 255, 255);
pMap.setFog(color, 0, 5000, 0.3);
```

{% endtab %}
{% endtabs %}

### getPathIntervalPositions(path, interval, isUnionTerrain) → [JSVec3Array](../core/jsvec3array.md)

> 경위도 경로를 일정 간격으로 나눈 좌표 목록을 반환합니다.

#### Parameters

| Name            | Type                                  | Description                        |
| --------------- | ------------------------------------- | ---------------------------------- |
| path            | [JSVec3Array](../core/jsvec3array.md) | 경위도 경로 좌표 목록              |
| interval        | number                                | 간격 (meter 단위)                  |
| isUnionTerrain  | boolean                               | true: 지형 반영, false: 단순 표면  |

#### Returns

- [JSVec3Array](../core/jsvec3array.md): 간격에 따라 분할된 좌표 목록

#### Sample

```javascript
let path = new Module.JSVec3Array();
path.push(new Module.JSVector3D(127.0, 37.5, 0));
path.push(new Module.JSVector3D(127.01, 37.51, 0));

let result = Module.getMap().getPathIntervalPositions(path, 50, true);
```

{% endtab %}
{% endtabs %}

### getTerrHeightFast(lon, lat) → number

> 입력한 경도(lon), 위도(lat) 기준의 지형 고도 값을 빠르게 반환합니다.  
> 일반 getTerrHeight보다 성능이 빠르지만, 정밀도는 약간 낮을 수 있습니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description             |
| ---- | ------ | ----------------------- |
| lon  | number | 경도 (degrees 단위)     |
| lat  | number | 위도 (degrees 단위)     |

- Return  
  - number: 지형 고도 값 (meter 단위)  
  - 0: 고도 요청 실패

{% endtab %}
{% tab title="Template" %}

```javascript
let lon = 127.0;
let lat = 37.5;
let height = Module.getMap().getTerrHeightFast(lon, lat);
```

{% endtab %}
{% endtabs %}

### getPositionByAngleDistance3D(position, distance, angle) → [JSVector3D](../core/jsvector3d.md)

> 기준 좌표(`position`)에서 주어진 거리(`distance`)와 방위각(`angle`)을 기반으로 계산된 위치를 반환합니다.  
> 방위각은 북쪽을 기준으로 시계 방향으로 증가합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                              |
| -------- | ----------------------------------- | ---------------------------------------- |
| position | [JSVector3D](../core/jsvector3d.md) | 기준 위치 (경도, 위도, 고도).            |
| distance | number                              | 이동 거리 (meters 단위).                 |
| angle    | number                              | 이동 방향 각도 (degrees, 북쪽 기준 시계방향). |

- Return  
  - [JSVector3D](../core/jsvector3d.md): 이동 결과 위치 (경도, 위도, 고도)

{% endtab %}
{% tab title="Template" %}

```javascript
let base = new Module.JSVector3D(127.0, 37.5, 100.0);
let result = Module.getMap().getPositionByAngleDistance3D(base, 100.0, 90.0);  // 동쪽으로 100m 이동
```

{% endtab %}
{% endtabs %}

### getAreaIntervalPositions(area, intervalVertical, intervalHorizontal, direction) → [JSVec3Array](../core/jsvec3array.md)

> 주어진 다각형 영역(`area`) 안에 일정 간격(`intervalVertical`, `intervalHorizontal`)으로 점을 분포시켜 반환합니다.  
> `direction` 값에 따라 정렬 방향을 조절할 수 있으며, 각 점은 실제 지형고도를 반영하여 3D 좌표로 반환됩니다.

{% tabs %}
{% tab title="Information" %}

| Name              | Type                                  | Description                                         |
| ----------------- | ------------------------------------- | --------------------------------------------------- |
| area              | [JSVec3Array](../core/jsvec3array.md) | 영역 경계 좌표 목록 (경도, 위도, 고도).               |
| intervalVertical  | number                                | 세로 간격 (meter 단위).                             |
| intervalHorizontal| number                                | 가로 간격 (meter 단위).                             |
| direction         | number                                | 정렬 기준 각도 (degrees). 북쪽 기준 시계방향으로 회전 |

- Return  
  - [JSVec3Array](../core/jsvec3array.md): 영역 내부 일정 간격으로 분포된 위치 리스트 (경도, 위도, 고도)

{% endtab %}
{% tab title="Template" %}

```javascript
let area = new Module.JSVec3Array();
area.push(new Module.JSVector3D(127.0, 37.5, 0));
area.push(new Module.JSVector3D(127.01, 37.5, 0));
area.push(new Module.JSVector3D(127.01, 37.51, 0));
area.push(new Module.JSVector3D(127.0, 37.51, 0));
area.push(new Module.JSVector3D(127.0, 37.5, 0));

let result = Module.getMap().getAreaIntervalPositions(area, 10, 10, 0);
```

{% endtab %}
{% endtabs %}

### setHeatMapOpacity(opacity)

> 히트맵의 투명도를 설정합니다.  
> 값이 작을수록 히트맵이 더 투명하게 표시됩니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type  | Description                      |
| ------- | ----- | -------------------------------- |
| opacity | float | 히트맵 투명도 (0.0 ~ 1.0 사이값). |

- `0.0`: 완전히 투명  
- `1.0`: 완전히 불투명

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getMap().setHeatMapOpacity(0.7);  // 히트맵 투명도 70%로 설정
```

{% endtab %}
{% endtabs %}

### setDefaultHeatMapColor()

> 히트맵 색상을 기본 색상으로 초기화합니다.

{% tabs %}
{% tab title="Information" %}

- 현재 설정된 사용자 정의 히트맵 색상 구성을 제거하고, 엔진 기본 색상 구성을 복원합니다.
- 히트맵 표현이 초기 상태로 재설정됩니다.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getMap().setDefaultHeatMapColor();
```

{% endtab %}
{% endtabs %}

### setHeatMapColor(colors)

> 히트맵 색상 구성 목록을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type                                | Description                      |
|--------|-------------------------------------|----------------------------------|
| colors | [Collection](../core/collection.md) | [JSColor](../core/jscolor.md)의 배열. |

- 최소 2개 이상의 색상이 필요합니다.
- 설정된 색상은 낮은 밀도부터 높은 밀도까지 순차적으로 적용됩니다.

{% endtab %}
{% tab title="Template" %}

```javascript
let colorList = new Module.Collection();
colorList.Add(new Module.JSColor(0, 0, 255));   // Low density - blue
colorList.Add(new Module.JSColor(0, 255, 0));   // Mid density - green
colorList.Add(new Module.JSColor(255, 0, 0));   // High density - red

Module.getMap().setHeatMapColor(colorList);
```

{% endtab %}
{% endtabs %}

### getPositionByAngleDistance3D(position, distance, angle) → [JSVector3D](../core/jsvector3d.md)

> 입력 위치로부터 특정 각도와 거리만큼 떨어진 지점의 좌표를 반환합니다.
>
> 반환 좌표는 경위도 및 고도 형태입니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                                       |
|----------|-------------------------------------|---------------------------------------------------|
| position | [JSVector3D](../core/jsvector3d.md) | 기준 위치 (경도, 위도, 고도).                    |
| distance | number                              | 거리 (meter 단위).                               |
| angle    | number                              | 방향 (degrees, 북쪽 기준 시계방향 각도 0~360도). |

- 거리 < 0 또는 각도가 0~360 범위를 벗어나면 null 벡터가 반환됩니다.

- 결과 좌표는 입력 기준점에서 북쪽 기준 angle 각도 방향으로 distance만큼 이동한 지점을 의미합니다.

{% endtab %}
{% tab title="Template" %}

```javascript
let center = new Module.JSVector3D(127.0, 37.5, 100); // 기준 위치
let offset = Module.getMap().getPositionByAngleDistance3D(center, 1000, 45); // 북동쪽 1km 위치
```

{% endtab %}
{% endtabs %}
