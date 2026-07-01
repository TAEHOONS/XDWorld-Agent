---
description: 지도 내 시계열 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSTimeSeriesObject

> Module.createTimeSeriesObject() API를 생성합니다.
>
> 생성 후 create() 혹은 createbyJson() API에 파라메터를 전달하여 시계열 데이터 초기화 합니다.
>
> 데이터 갱신이 필요할 경우, insert(), merge() 순으로 함수를 호출하여 데이터 갱신.

```javascript
let object = Module.createTimeSeriesObject("ID");

// For detailed parameters, refer to the API documentation
object.create(/*parameter*/);
// ... or ...
object.createJSON(/*parameter*/);
// ... or ...
object.insert(/*parameter*/);
// ... or ...
object.merge(/*parameter*/);
```

## Function

### create(parameter) → object

> 시계열 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type                                                                                  | Description |
| :-------- | :------------------------------------------------------------------------------------ | :---------- |
| parameter | [JSTimeSeriesObject.ObjectData](jstimeseriesobject.md##jstimeseriesobject.objectdata) | 속성 정보.  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 ( 문자열 : 실패 에러 코드 ).

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### createbyJson(parameter) → object

> 시계열 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type                                                                                  | Description |
| :-------- | :------------------------------------------------------------------------------------ | :---------- |
| parameter | [JSTimeSeriesObject.ObjectData](jstimeseriesobject.md##jstimeseriesobject.objectdata) | 속성 정보.  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 ( 문자열 : 실패 에러 코드 ).

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### insert(parameter) → object

> 새로운 시계열 데이터를 추가합니다.
>
> 이후 [merge()](jstimeseriesobject.md#merge-object)를 호출하여 입력한 데이터를 기존 객체에 추가하는 작업 필요합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type                                                                                  | Description |
| :-------- | :------------------------------------------------------------------------------------ | :---------- |
| parameter | [JSTimeSeriesObject.ObjectData](jstimeseriesobject.md##jstimeseriesobject.objectdata) | 속성 정보.  |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 ( 문자열 : 실패 에러 코드 ).

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### merge() → object

> [insert()](jstimeseriesobject.md#insert-parameter-object)로 입력한 데이터를 기존 시계열 객체에 추가합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 ( 문자열 : 실패 에러 코드 ).

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### Type Definitions

#### JSTimeSeriesObject.ObjectData

> 시계열 객체 생성 정보.

| Name       | Type                                                                                | Attributes | Default                                           | Description                                               |
| ---------- | ----------------------------------------------------------------------------------- | ---------- | ------------------------------------------------- | --------------------------------------------------------- |
| position   | [JSVector3D](../core/jsvector3d.md)                                                 |            |                                                   | 중심 좌표 (경도, 위도, 고도).                             |
| segment    | number                                                                              | optional   | 4                                                 | 평면 형태 (2: 평면, 3: 삼각형, 4: 사각형, 5: 오각형).     |
| rotate     | number                                                                              | optional   | 0                                                 | 객체 회전 (0,360: north, 90: east, 180: south, 270: west) |
| horizontal | number                                                                              | optional   | 5.0                                               | 시계열 객체의 가로 크기 설정.                             |
| vertical   | number                                                                              | optional   | 5.0                                               | 시계열 객체의 세로 크기 설정.                             |
| shape      | number                                                                              | optional   | 0                                                 | 객체 형태 (0: 3D 다각면, 1: 2D 평면)                      |
| color      | [JSColor](../core/jscolor.md)                                                       | optional   | [JSColor](../core/jscolor.md)(255, 255, 255, 255) | 객체 색상.                                                |
| area       | [JSTimeSeriesObject.AreaData](jstimeseriesobject.md##jstimeseriesobject.areadata)   | optional   |                                                   | 객체 크기 (이미지 연산이 필요).                           |
| image      | [JSTimeSeriesObject.ImageData](jstimeseriesobject.md##jstimeseriesobject.imagedata) |            |                                                   | 이미지 정보.                                              |
| legend     | [JSTimeSeriesObject.Legend](jstimeseriesobject.md##jstimeseriesobject.legend)       | optional   | [JSColor](../core/jscolor.md)(255, 255, 255, 255) | 범례 생성 정보.                                           |

#### JSTimeSeriesObject.AreaData

> 시계열 객체의 크기를 설정합니다.

| Name | Type                                | Attributes | Default                                      | Description                        |
| ---- | ----------------------------------- | ---------- | -------------------------------------------- | ---------------------------------- |
| min  | [JSVector3D](../core/jsvector3d.md) | optional   | [JSVector3D](../core/jsvector3d.md)(0, 0, 0) | 최소 영역 좌표 (경도, 위도, 고도). |
| max  | [JSVector3D](../core/jsvector3d.md) | optional   | [JSVector3D](../core/jsvector3d.md)(0, 0, 0) | 최대 영역 좌표 (경도, 위도, 고도). |

#### JSTimeSeriesObject.ImageData

| Name   | Type   | Description    |
| ------ | ------ | -------------- |
| width  | number | 이미지 너비.   |
| height | number | 이미지 높이.   |
| data   | object | 이미지 데이터. |

#### JSTimeSeriesObject.Legend

> Legend data. Store multiple data and color items grouped together in an array.

| Name  | Type                                                                          | Description     |
| ----- | ----------------------------------------------------------------------------- | --------------- |
| data  | number                                                                        | 범례 구간 크기. |
| color | [JSColor](../core/jscolor.md) or array (array defining argb with four floats) | 범례의 색상값.  |
