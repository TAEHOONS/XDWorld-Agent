---
description: 지도 내 지잔파 분석 기능 설정을 위한 API입니다.
---

# JSEarthquake

> Module.getEarthquake API를 생성합니다.

```javascript
var earthquake = Module.getEarthquake();
```

## Function

### Clear() → boolean

> 지진파 분석을 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true: 초기화 성공.
    -   false: 초기화 실패.
    -   실패 조건
        -   지도 갱신이 안된 경우.
        -   지진파 분석 결과가 없는 경우.

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### SetResolution(resolution) → boolean

> 지진파 분석 반경을 설정합니다.
>
> 입력 변수값을 통해 가로 세로 정사각형 영역을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type   | Description                    |
| ---------- | ------ | ------------------------------ |
| resolution | number | 지진파 분석 반경 (meter 단위). |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   0.001보다 작은 지진파 반경이 설정된 경우.

-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Earthquake Wave](https://sandbox.egiscloud.com/code/main.do?id=object_earthquakewave)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### SetHeightWeight(height) → boolean

> 지진파 분석 높이를 설정합니다.
>
> 입력 변수값을 기준으로 지진파 높이 비율 파형을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description                         |
| ------ | ------ | ----------------------------------- |
| height | number | 지진파 최대 표현 높이 (meter 단위). |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.
    -   실패 조건
        -   0.01보다 작은 지진파 높이가 설정된 경우.
        -   200보다 큰 값이 설정된 경우.

-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Earthquake Wave](https://sandbox.egiscloud.com/code/main.do?id=object_earthquakewave)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### SetBaseAltitude(altitude) → boolean

> 지진 근원지 높이를 설정합니다.
>
> 입력 변수값을 기준으로 지진 근원지 높이를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type   | Description                    |
| -------- | ------ | ------------------------------ |
| altitude | number | 지진 근원지 높이 (meter 단위). |

-   Return

    -   true: 설정 성공.
    -   false: 설정 실패.

-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Earthquake Wave](https://sandbox.egiscloud.com/code/main.do?id=object_earthquakewave)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### GetEarthquakeData(url, position) → boolean

> 가시화 지진파 객체를 생성합니다.
>
> 입력된 url을 통해 지진파 파일 포맷을 요청합니다.
>
> 지진파 파일 포맷을 통해 가시화 될 지진파 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name     | Type                                | Description                              |
| -------- | ----------------------------------- | ---------------------------------------- |
| url      | string                              | 파일 주소(.eqs)                          |
| position | [JSVector2D](../core/jsvector2d.md) | 지진 근원지 생성 위치 좌표 (경도, 위도). |

-   Return

    -   true: 생성 성공.
    -   false: 생성 실패.

-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Earthquake Wave](https://sandbox.egiscloud.com/code/main.do?id=object_earthquakewave)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}
