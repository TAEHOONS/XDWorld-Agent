---
description: 지도 내 파이프 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSPipe

> Module.createPipe() API를 생성합니다.

```javascript
var object = Module.createPipe("ID");
```

## Function

### create(coordinates, startColor, endColor, segment, radius, width) → boolean

> 3d 파이프 객체를 생성합니다.
>
> 입력 변수값(segment)은 3보다 큰값이 설정됩니다.
>
> 입력 변수값(radius)은 0보다 큰값이 설정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type                                | Description                  |
| :---------- | :---------------------------------- | :--------------------------- |
| coordinates | [Collection](../core/collection.md) | 좌표 목록(경도, 위도, 고도). |
| startColor  | [JSColor](../core/jscolor.md)       | 시작 파이프 색상.            |
| endColor    | [JSColor](../core/jscolor.md)       | 끝 파이프 색상.              |
| segment     | number                              | 단면의 다각수.               |
| radius      | number                              | 반지름.                      |
| width       | number                              | 파이프 표현시 두께 설정.     |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
-   Sample
    -   function createUndergroundFacility 참조.
    -   [Sandbox_Creating Excavation](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_create)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getExtent() → number

> 3d 파이프 객체의 공간 영역의 장축 거리를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 거리 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript
var bExtends = figure.getExtent();
```

{% endtab %}
{% endtabs %}

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

### getPositions() → [JSVec3Array](../core/jsvec3array.md)

> 3d 파이프 객체을 중심 좌표(경도, 위도, 고도)를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSVec3Array](../core/jsvec3array.md): 반환 성공.
    -   null: 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getRadius() → number

> 3d 파이프 객체을 반지름(meter 단위)을 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number: 반환 성공.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### moveVertically(altitude) → boolean

> 3d 파이프 객체의 고도를 설정합니다.
>
> 입력 변수값(altitude) 최소 -1000 보다 큰 값이 입력 되어야 합니다(해발고도 기준).

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description |
| :------- | :----- | :---------- |
| altitude | number | 고도 설정.  |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setColor(starColor, endColor) → boolean

> 3d 파이프 객체의 시작, 끝에 대한 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type                          | Description |
| :--------- | :---------------------------- | :---------- |
| startColor | [JSColor](../core/jscolor.md) | 시작 색상.  |
| endColor   | [JSColor](../core/jscolor.md) | 끝 색상.    |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setFlow(startColor, endColor, segment, interval) → boolean

> 3d 파이프 객체 내부 흐름 표현 형태를 설정합니다.
>
> 입력 변수값(segment)은 3보다 큰값이 설정됩니다.
>
> 입력 변수값(interval)은 0보다 큰값이 설정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type                          | Description              |
| :--------- | :---------------------------- | :----------------------- |
| startColor | [JSColor](../core/jscolor.md) | 시작 색상.               |
| endColor   | [JSColor](../core/jscolor.md) | 끝 색상.                 |
| segment    | number                        | 흐름 구성을 위한 점수.   |
| interval   | number                        | 흐름 표현 화살표의 간격. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function createUndergroundFacility 참조.
    -   [Sandbox_Creating Excavation](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_create)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setFlowDisplay(type) → boolean

> 3d 파이프 객체 내부 흐름 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                        |
| :--- | :------ | :------------------------------------------------- |
| type | boolean | <p>true: 흐름 가시화.<br>false: 흐름 비가시화.</p> |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function createUndergroundFacility 참조.
    -   [Sandbox_Creating Excavation](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_create)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setFlowWaitFrame(farme) → boolean

> 3d 파이프 내부 흐름에 대한 갱신 프레임 수를 설정합니다.
>
> 입력 변수값(frame)은 0보다 큰값이 설정됩니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description     |
| :---- | :----- | :-------------- |
| frame | number | 갱신 프레임 수. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function createUndergroundFacility 참조.
    -   [Sandbox_Creating Excavation](https://sandbox.egiscloud.com/code/main.do?id=analysis_transparency_create)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setSimplifyRange(range) → boolean

> 3d 파이프 객체의 간소화 표현 거리를 설정합니다.
>
> 입력 변수값(range)은 0보다 큰값이 설정됩니다.
>
> 간소화 표현 중 흐름 표현은 생략됩니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description  |
| :---- | :----- | :----------- |
| range | number | 간소화 거리. |

-   Return
    -   true: 설정 성공.
    -   false: 설정 실패.
-   Sample
    -   function createPipe 참조.
    -   [Sandbox_Pipe](https://sandbox.egiscloud.com/code/main.do?id=object_pipe)

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
