---
description: 지도 내 멀티 POI 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSMultiPoint

> Module.createMultiPoint() API를 생성합니다.

```javascript
var object = Module.createMultiPoint("ID");
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

### setMainPoint(id, position, icon) → boolean

> 멀티 POI 객체를 생성합니다.
>
> 중심 좌표(경도, 위도, 고도)를 기준으로 main POI를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                   |
| :------- | :---------------------------------- | :---------------------------- |
| id       | string                              | 고유 명칭.                    |
| position | [JSVector3D](../core/jsvector3d.md) | 위치 좌표 (경도, 위도, 고도). |
| icon     | [JSIcon](./jsicon.md)               | POI 이미지.                   |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
-   Sample
    -   function initPage 참조.
    -   [Sandbox_MultiPoint](https://sandbox.egiscloud.com/code/main.do?id=object_multipoint)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setMainPointVisible(visible) → boolean

> main POI 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                              |
| :------ | :------ | :--------------------------------------- |
| visible | boolean | <p>true: 가시화.<br>false: 비가시화.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
object.setMainPointVisible(true); // Visible On
object.setMainPointVisible(false); // Visible Off
```

{% endtab %}
{% endtabs %}

### setSpreadEffect(set) → boolean

> 카메라와 멀티 POI 간 거리에 따라 sub POI 표출 애니메이션을 설정합니다.
>
> 표출 애니메이션 설정 시 sub POI는 카메라 거리에 따라 중심으로 부터 바깥 방향으로 이동합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                               |
| :--- | :------ | :-------------------------------------------------------- |
| set  | boolean | <p>true: 표출 애니메이션 사용.<br>false: 일반 가시화.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
object.setSpreadEffect(true); // Effect On
object.setSpreadEffect(false); // Effect Off
```

{% endtab %}
{% endtabs %}

### insertSubPoint(id, icon) → boolean

> main POI에 속하는 sub POI 객체를 추가합니다.
>
> 중심 좌표(경도, 위도, 고도)를 기준으로 시계 방향 순으로 자동 배치되는 sub POI를 추가합니다.
>
> 객체의 고유 명칭 구성은 (메인 POI 명칭)#(입력받는 name)로 구성

{% tabs %}
{% tab title="Information" %}

| Name | Type                  | Description |
| :--- | :-------------------- | :---------- |
| id   | string                | 고유 명칭.  |
| icon | [JSIcon](./jsicon.md) | POI 이미지. |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   function createSubPoints 참조.
    -   [Sandbox_MultiPoint](https://sandbox.egiscloud.com/code/main.do?id=object_multipoint)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setBar(color, altitude, width) → boolean

> main POI 중심 좌표(경도, 위도, 고도)로 부터 지형을 연결하는 선 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                          | Description            |
| :------- | :---------------------------- | :--------------------- |
| color    | [JSColor](../core/jscolor.md) | 선 색상.               |
| altitude | number                        | 선을 높이(meter 단위). |
| width    | number                        | 선을 두께.             |

-   Return
    -   true: 추가 성공.
    -   false: 추가 실패.
-   Sample
    -   function createMultiPoint 참조.
    -   [Sandbox_MultiPoint](https://sandbox.egiscloud.com/code/main.do?id=object_multipoint)

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
