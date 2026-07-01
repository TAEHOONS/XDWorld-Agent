---
description: 지도 내 시야 분석 기능 설정을 위한 API입니다.
---

# JSSightAnalysis

> Module.getSightAnalysis() API를 생성합니다.

```javascript
var sightAnalysis = Module.getSightAnalysis();
```

## Function

### GetObjectPositionsOnPath(coordinates, hbuffer, vbuffer, layer) → [JSSightAnalysis.ObjectOnPathResult](jssightanalysis.md#jssightanalysis.objectonpathresult)

> Returns the distance and position of objects from a specified path.
>
> Analyzes based on the path's milestone distance for objects within the range, based on the search range along the path.
>
> The hbuffer input value is the horizontal buffer size. The larger the value, the wider the range of objects analyzed horizontally.
>
> The vbuffer input value is the vertical buffer size. The larger the value, the wider the range of objects analyzed vertically.

> 지정된 경로에서 객체까지의 거리, 위치를 반환합니다.
>
> 경로에 검색 범위를 바탕으로 범위 내에 존재하는 객체에 대한 경로의 이정 거리 기준으로 분석합니다.
>
> 입력 변수값(hbuffer)은 수평 버퍼 크기로 값이 클수록 수평으로 넓은 범위의 객체를 분석합니다.
>
> 입력 변수값(vbuffer)은 수직 버퍼 크기로 값이 클수록 수직으로 넓은 범위의 객체를 분석합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                                                                                       |
| :---------- | :------------------------------------ | :------------------------------------------------------------------------------------------------ |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | ([JSVector3D](../core/jsvector3d.md), [JSVector3D](../core/jsvector3d.md), ...) 분석할 경로 배열. |
| hbuffer     | number                                | 수평 버퍼 크기.                                                                                   |
| vbuffer     | number                                | 수직 버퍼 크기.                                                                                   |
| layer       | [JSLayer](../layer/jslayer.md)        | 분석할 객체를 포함한 레이어.                                                                      |

-   Return
    -   [JSSightAnalysis.ObjectOnPathResult](jssightanalysis.md#jssightanalysis.objectonpathresult): 지정된 경로 진행중 오브젝트와 수직 방향으로 만나는 지점들의 위치를 반환합니다.
-   Sample
    -   function analysisPositions 참조.
    -   [Sandbox_Path Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_line_path_distance)

{% endtab %}
{% tab title="Template" %}

```javascript
var coordinates = Module.getMap().getInputPoints();
var returnJSON = Module.getSightAnalysis().GetObjectPositionsOnPath(coordinates, 30.0, 5.0, "analysis layer");

let returnJSON = "{
	[
		{
			Longitude : 129.2,
			Latitude : 36.8,
			Altitude : 10.2,
			ObjectKey : "Test1",
			Distance : 10,
			Side : "Left"
		},
		{
			Longitude : 129.222,
			Latitude : 36.811,
			Altitude : 13.5,
			ObjectKey : "Test2",
			Distance : 30,
			Side : "Right"
		},
	]
```

{% endtab %}
{% endtabs %}

### Type Definitions

#### JSSightAnalysis.ObjectOnPathResult

> GetObjectPositionsOnPath 기능을 통해 분석된 결과 데이터 포맷입니다.
>
> json 구조를 가진 문자열로 반환됩니다.

| Name   | Type                                                                                                                 | Description                   |
| ------ | -------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| return | array([JSSightAnalysis.ObjectOnPathResult.Position](jssightanalysis.md#jssightanalysis.objectonpathresult.position)) | 개별 분석에 대한 결과 데이터. |

#### JSSightAnalysis.ObjectOnPathResult.Position

> Unit object information of [JSSightAnalysis.ObjectOnPathResult](jssightanalysis.md#jssightanalysisobjectonpathresult)

| Name      | Type   | Description                                                         |
| --------- | ------ | ------------------------------------------------------------------- |
| Longitude | number | 분석에 포함된 객체의 경도.                                          |
| Latitude  | number | 분석에 포함된 객체의 위도.                                          |
| Altitude  | number | 분석에 포함된 객체의 고도.                                          |
| ObjectKey | string | 분석에 포함된 객체의 고유 키.                                       |
| Distance  | number | 검출된 객체의 경로상 이정 거리.                                     |
| Side      | string | 검출된 객체가 경로상 좌측, 우측여부 (좌측 : "Left", 우측 : "Right). |
