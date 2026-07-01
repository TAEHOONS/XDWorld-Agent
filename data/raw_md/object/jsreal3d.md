---
description: 지도 내 시설물 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSReal3D

> Module.createReal3D() API를 생성합니다.
>
> JSReal3D는 시설물(건물) 형태를 출력하는 오브젝트 입니다.ㅏ

```javascript
var object = Module.createReal3D("ID");
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

### setElevationSectionColor(elevation, color) → boolean

> 시설물 객체에 대한 층별 색상 리스트를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type                                | Description |
| --------- | ----------------------------------- | ----------- |
| elevation | [Collection](../core/collection.md) | 고도 목록.  |
| color     | [Collection](../core/collection.md) | 색상 목록.  |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var elevationList = new Module.Collection();
//.. add elevation values ..
var colorList = new Module.Collection();
//.. add color values ..
object.setElevationSectionColor(elevationList, colorList);
```

{% endtab %}
{% endtabs %}

### setFillColor(type, color) → boolean

> 시설물 객체의 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description                                              |
| ----- | ----------------------------- | -------------------------------------------------------- |
| type  | boolean                       | <p>true: 심플렌더링 설정.<br>false: 일반 렌더링 설정.<p> |
| color | [JSColor](../core/jscolor.md) | 색상값.                                                  |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setShaderType(type) → boolean

> 시설물 객체의 층별 색상 표시 방식을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                                        |
| ---- | ------ | -------------------------------------------------- |
| type | number | <p>0: 이미지.<br>1: 이미지 + 색상.<br>2: 색상.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
object.setShaderType(1);
```

{% endtab %}
{% endtabs %}

### setStyle(style) → boolean

> 시설물 객체의 스타일을 설정합니다.
>
> 시설물 객체는 색상 스타일만 설정 가능합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                                  | Description       |
| ----- | ------------------------------------- | ----------------- |
| style | [JSPolygonStyle](./jspolygonstyle.md) | 스타일 속성 정보. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var polyStyle = new Module.JSPolygonStyle();
polyStyle.setFill(true);
polyStyle.setFillColor(new Module.JSColor(255, 255, 0, 0));
//...
object.setStyle(polyStyle);
```

{% endtab %}
{% endtabs %}

### getFillColor() → [JSColor](../core/jscolor.md)

> 시설물 객체의 색상을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSColor](../core/jscolor.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getPosition() → [JSVector3D](../core/jsvector3d.md)

> 시설물 객체의 중심 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVector3D](../core/jsvector3d.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getHeight() → number

> 시설물 객체의 높이값(in meter)을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number : 반환 성공.

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
