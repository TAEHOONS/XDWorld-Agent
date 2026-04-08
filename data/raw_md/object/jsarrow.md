---
description: 지도 내 3차원 모델 화살표 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSArrow

> Module.CreateArrow() API를 생성합니다.

```javascript
var object = Module.CreateArrow("ID");
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
var strKey = object.getId();
```

{% endtab %}
{% endtabs %}

### Create(position, pan, tilt, distance, radius, head_rate, arrow_radius, color) → boolean

> 3차원 모델 화살표 객체를 생성합니다.
>
> pan 입력 값에 따른 회전 정보
>
> -   0, 360 (북쪽).
> -   90 (동쪽).
> -   180 (남쪽).
> -   270 (서쪽).
>
> 기울기 입력 값에 따른 회전 정보
>
> -   0 (정면).
> -   tilt \< 0 (위쪽).
> -   tilt \> 0 (아래쪽).

{% tabs %}
{% tab title="Information" %}

| Name         | Type                                | Description            |
| ------------ | ----------------------------------- | ---------------------- |
| position     | [JSVector3D](../core/jsvector3d.md) | 화살표 시작 경위도.    |
| pan          | number                              | 화살표 Y축 회전 설정.  |
| tilt         | number                              | 화살표 X축 회전 설정.  |
| distance     | number                              | 화살표 전체 길이 설정. |
| radius       | number                              | 화살대 굵기 지정.      |
| head_rate    | number                              | 화살촉 비율.           |
| arrow_radius | number                              | 화살촉 굵기 지정.      |
| color        | [JSColor](../core/jscolor.md)       | 화살표 색상 지정.      |

-   Return
    -   true : 생성 성공.
    -   false : 생성 실패.
-   Sample
    -   the init function 참조.
    -   [Sandbox_Arrow(3D)](https://sandbox.egiscloud.com/code/main.do?id=object_arrow)

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
var objVisible = object.getVisible();
// ... or ...
object.setVisible(true);
```

{% endtab %}
{% endtabs %}

### getPosition(), setPosition(pos) → void

> 화살표 객체의 시작점을 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type                                | Description        |
| ---- | ----------------------------------- | ------------------ |
| pos  | [JSVector3D](../core/jsvector3d.md) | 화살표 객체의 시작점. |

{% endtab %}
{% tab title="Template" %}

```javascript
var startPos = object.getPosition();
// ... or ...
object.setPosition(pos);
```

{% endtab %}
{% endtabs %}

### getOrient(), setOrient(orient) → void

> 화살표 객체의 방향을 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description      |
| ------ | ------ | ---------------- |
| orient | number | 화살표 객체의 방향 |

{% endtab %}
{% tab title="Template" %}

```javascript
var dir = object.getOrient();
// ... or ...
object.setOrient(orient);
```

{% endtab %}
{% endtabs %}

### getTilt(), setTilt(tilt) → void

> 화살표 객체의 틸트를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description      |
| ---- | ------ | ---------------- |
| tilt | number | 화살표 객체의 틸트 |

{% endtab %}
{% tab title="Template" %}

```javascript
var tilt = object.getTilt();
// ... or ...
object.setTilt(tilt);
```

{% endtab %}
{% endtabs %}

### getDist(), setDist(dist) → void

> 객체의 길이를 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description      |
| ---- | ------ | ---------------- |
| dist | number | 화살표 객체의 길이 |

{% endtab %}
{% tab title="Template" %}

```javascript
var dist = object.getDist();
// ... or ...
object.setDist(dist);
```

{% endtab %}
{% endtabs %}

### getColor(), setColor(color) → void

> 객체의 색상을 설정 및 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description      |
| ----- | ----------------------------- | ---------------- |
| color | [JSColor](../core/jscolor.md) | 화살표 객체의 색상 |

{% endtab %}
{% tab title="Template" %}

```javascript
var color = object.getColor();
// ... or ...
object.setColor(color);
```

{% endtab %}
{% endtabs %}