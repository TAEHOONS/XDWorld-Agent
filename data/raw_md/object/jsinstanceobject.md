---
description: 지도 내 인스턴스 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSInstanceObject

> Module.createInstanceObject API를 생성합니다.

```javascript
let instanceObject = Module.createInstanceObject("object");
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

### getIntersectObjects(parameter) → error

> 등록된 인스턴스 객체와 입력 변수값(parameter)에서 설정된 직선과 겹치는 항목을 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type                                                                                                         | Description     |
| --------- | ------------------------------------------------------------------------------------------------------------ | --------------- |
| parameter | [JSInstanceObject.IntersectObjectsParameter](jsinstanceobject.md#jsinstanceobject.intersectobjectsparameter) | 비교 속성 정보. |

-   Return
    -   .result: API 성공 유무 상태 ( 1 : 성공, 0 : 실패 ).
    -   .name: 동작 API 명칭.
    -   .return: API 반환 정보 ( object : 정상적인 반환값, 문자열 : 실패 에러 코드 ).

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getAlpha(), setAlpha(alpha) → number

> 인스턴스 객체 투명도를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description |
| ----- | ------ | ----------- |
| alpha | number | 투명도.     |

-   Return
    -   number: 설정된 투명도.

{% endtab %}
{% tab title="Template" %}

```javascript
let instanceObject = Module.createInstanceObject("object");
let alpha = instanceObject.getAlpha();
// ... or ...
let instanceObject = Module.createInstanceObject("object");
instanceObject.setAlpha(0.5);
```

{% endtab %}
{% endtabs %}

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

### Type Definitions

#### JSInstanceObject.IntersectObjectsParameter

> 등록된 인스턴스 객체와 겸침 유무 정보를 설정합니다.

| Name        | Type                                                                                                                                 | Default | Description                  |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------- | ---------------------------- |
| objectType  | string                                                                                                                               | "line"  | 객체 타입(점, 선, 면).       |
| coordinates | [JSInstanceObject.IntersectObjectsParameter.coordinates](jsinstanceobject.md#jsinstanceobject.intersectobjectsparameter.coordinates) |         | 좌표 목록(경도, 위도, 고도). |

#### JSInstanceObject.IntersectObjectsParameter.coordinates

| Name        | Type   | Description                                                                                                                                                                                                                                                           |
| ----------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| style       | string | 좌표 변환 타입. 아래 네 가지에 해당되지 않는 경우, 오류 발생.<br>XY : 경위도 배열 값 [x, y], [x, y]</br><br>XYZ : 경위고도 배열 값 [x, y, z], [x, y, z]</br><br>XYZARRAY : 경위고도 배열 값 [x, y, z, x, y, z]</br><br>JSVector3D : 경위고도 JSVec3Array 배열 값</br> |
| coordinates | number | 좌표 목록(경도, 위도, 고도).                                                                                                                                                                                                                                          |
