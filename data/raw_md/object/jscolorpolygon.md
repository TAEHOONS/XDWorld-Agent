---
description: 지도 내 그라데이션 폴리곤 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSColorPolygon

> Module.createColorPolygon() API를 생성합니다.

```javascript
var colorPolygon = Module.createColorPolygon("ID");
```

## Function

### getId() → string

> 객체의 고유 명칭을 반환 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   string: 객체 설명 문자열이 성공적으로 반환.
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
let parameter = object.getId();
```

{% endtab %}
{% endtabs %}

### SetVerticalPlane(coordinates, parts, height, startColor, endColor) → boolean

> 수직 벽 폴리곤 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                  | Description                 |
| ----------- | ------------------------------------- | --------------------------- |
| coordinates | [JSVec3Array](../core/jsvec3array.md) | 폴리곤 경위도 좌표 목록.    |
| parts       | [Collection](../core/collection.md)   | 폴리곤 구성 점정 개수 목록. |
| height      | number                                | 폴리곤 높이.                |
| startColor  | [JSColor](../core/jscolor.md)         | 그라데이션 시작 색상.       |
| endColor    | [JSColor](../core/jscolor.md)         | 그라데이션 끝 색상.         |

-   Return
    -   true : 생성 성공.
    -   false : 생성 실패.
    -   실패 조건
        -   입력된 coordinates 구성요소가 없거나 정점 개수가 2개 이하인 경우.
        -   입력된 parts 구성요소가 없거나 1개 이하인 경우.
-   Sample
    -   function createVerticalPlane 참조.
    -   [Sandbox_Polygon Gradient](https://sandbox.egiscloud.com/code/main.do?id=object_colorpolygon_gradation)

{% endtab %}
{% tab title="Template" %}

```javascript
var colorPolygon = Module.createColorPolygon("TEST_VERTICAL_POLYGON");

var basePositions = [
    [129.12599597147187, 35.17339329004985, 50.0],
    [129.1264736891435, 35.172432534300555, 50.0],
    [129.12705822860582, 35.172119138064076, 50.0],
    [129.12837813524428, 35.17198042514761, 50.0],
    [129.12925806742587, 35.171677294599604, 50.0],
    [129.13014427905534, 35.1712405752301, 50.0],
    [129.13067851056573, 35.170639446735436, 50.0],
];

var coordinates = new Module.JSVec3Array();
var parts = new Module.Collection();

for (var i = 0; i < basePositions.length; i++) {
    coordinates.push(new Module.JSVector3D(basePositions[i][0], basePositions[i][1], basePositions[i][2]));
}
parts.add(basePositions.length);

colorPolygon.SetVerticalPlane(coordinates, parts, -50.0, new Module.JSColor(0, 255, 255, 0), new Module.JSColor(255, 255, 0, 0));
```

{% endtab %}
{% endtabs %}

### SetCullMode(type) → boolean

> 수직 벽면 폴리곤 컬링 옵션 설정.
>
> type 입력 값에 따른 컬링 옵션은 0(양면), 1(양면), 2(CW) 3(CCW).
>
> 컬링 옵션 초기 설정 3.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description     |
| ---- | ------ | --------------- |
| type | number | 폴리곤 컬링모드 |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
-   Sample
    -   function createVerticalPlane 참조.
    -   [Sandbox_Polygon Gradient](https://sandbox.egiscloud.com/code/main.do?id=object_colorpolygon_gradation)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getDescription(), setDescription(desc) → string

> 객체에 대한 설명을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| ---- | ------ | ------------ |
| desc | string | 설명 문자열. |

-   Return
    -   string: 객체 설명 문자열이 성공적으로 반환.
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var strDesc = object.getDescription();
// ... or ...
object.setDescription("First Object.");
```

{% endtab %}
{% endtabs %}

### getName(), setName(name) → string

> 객체 이름을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| name | string | 객체 이름.  |

-   Return
    -   string: 객체 이름을 성공적을 반환
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var objName = object.getName();
// ... or ...
object.setName("MyObject");
```

{% endtab %}
{% endtabs %}

### getVisible(), setVisible(visible) → boolean

> 객체의 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                                        |
| ------- | ------- | -------------------------------------------------- |
| visible | boolean | <p>true: 객체 가시화.<br>false: 객체 비가시화.</p> |

-   Return
    -   true: 객체 가시화 상태.
    -   false: 객체 비가시화 상태.

{% endtab %}
{% tab title="Template" %}

```javascript
var objName = object.getName();
// ... or ...
object.setVisible(true);
```

{% endtab %}
{% endtabs %}

### setOpacity(opacity) → void

> 객체의 투명도(0.0 ~ 1.0)를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description             |
| ------- | ------- | ----------------------- |
| visible | boolean | 객체 투명도 값(0.0 ~ 1.0) |

{% endtab %}
{% tab title="Template" %}

```javascript
object.setOpacity(0.5);
```

{% endtab %}
{% endtabs %}

### toLonlatArray() → object

> 구성된 좌표 목록을 경위도, 고도로 반환합니다.

{% tabs %}
{% tab title="Information" %}

- Return
  - object
    - result: 1 → 생성 성공 / 0 → 실패
    - data: 좌표 데이터
    - return: 메시지

{% endtab %}
{% tab title="Template" %}

```javascript
var positions = object.toLonlatArray();
```

{% endtab %}
{% endtabs %}