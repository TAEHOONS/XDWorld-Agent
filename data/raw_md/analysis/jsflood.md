---
description: 지도 내 물판 기능 설정을 위한 API입니다.
---

# JSFlood

> Module.getFlood API를 생성합니다.

```javascript
var flood = Module.getFlood();
```

## Function

### active(active)

> 물판 애니메이션을 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type    | Description                                                        |
| :----- | :------ | :----------------------------------------------------------------- |
| active | boolean | <p>true: 물판 애니메이션 동작.<br>false: 물판 애니메이션 중지.</p> |

-   Sample
    -   function init 참조.
    -   [Sandbox_Flood](https://sandbox.egiscloud.com/code/main.do?id=weather_flood)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setColor(color)

> 물판 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description     |
| :---- | :---------------------------- | :-------------- |
| color | [JSColor](../core/jscolor.md) | 물판 변경 색상. |

-   Sample
    -   function SetFloodColor 참조.
    -   [Sandbox_Flood](https://sandbox.egiscloud.com/code/main.do?id=weather_flood)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setHeight(height)

> 물판 위치에 대한 고도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description                                |
| :----- | :----- | :----------------------------------------- |
| height | number | 해발고도 기준 물판 고도 설정 (meter 단위). |

-   Sample
    -   Refer to function setFloodHeight.
    -   [Sandbox_Flood](https://sandbox.egiscloud.com/code/main.do?id=weather_flood)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setVisibleAltitude(distance)

> 물판 가시거리를 설정합니다.
>
> 설정값이 클수록 먼 거리에서 물판 가시화가 가능합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description              |
| :------- | :----- | :----------------------- |
| distance | number | 가시 거리 (meters 단위). |

-   Sample
    -   function setFloodVisibleAltitude 참조.
    -   [Sandbox_Flood](https://sandbox.egiscloud.com/code/main.do?id=weather_flood)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setWaterSpeed(speed)

> 물판에서 물흐름 속도를 설정합니다.
>
> 설정값이 클수록 유속이 빨라집니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type   | Description    |
| :---- | :----- | :------------- |
| speed | number | 물판 유속 속도 |

-   Sample
    -   function SetWaterSpeed 참조.
    -   [Sandbox_Flood](https://sandbox.egiscloud.com/code/main.do?id=weather_flood)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### visibleWaterPlane(type)

> 물판에서 물흐름 표현 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type    | Description                                            |
| :--- | :------ | :----------------------------------------------------- |
| type | boolean | <p>true: 물판 유속 동작.<br>false: 물판 유속 중지.</p> |

-   Sample
    -   function visibleWaterPlane 참조.
    -   [Sandbox_Flood](https://sandbox.egiscloud.com/code/main.do?id=weather_flood)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}
