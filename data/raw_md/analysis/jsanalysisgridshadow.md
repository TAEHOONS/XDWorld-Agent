---
description: 지도 내 수인한도 분석 기능 설정을 위한 API 입니다.
---

# JSAnalysisGridShadow

> Module.getAnalysisGridShadow API를 생성합니다.

```javascript
var gridShadow = Module.getAnalysisGridShadow();
```

## Properties

| Name     			| Type                                	| Description                   |
| ----------------- | ------------------------------------- | ----------------------------- |
| strictCalculate 	| number                             	| 분석 옵션([Shadow Analysis Type List](../etc/type-list.md#shadow-analysis-type-list)). 			|

## Function

### clear() → boolean

> 생성된 수인한도 분석 결과를 초기화 합니다.
>
> 가시화 된 격자, 선택 객체를 해제 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   true: 초기화 성공.
    -   false: 초기화 실패.
    -   실패 조건
        -   생성 격자가 없는 경우.
        -   수인한도 분석에 사용할 레이어가 없는 경우.
-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Grid Shadow](https://sandbox.egiscloud.com/code/main.do?id=analysis_grid_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript
var gridShadow = Module.getAnalysisGridShadow();
gridShadow.clear();
```

{% endtab %}
{% endtabs %}

### create(layerName, gap, isClip) → boolean

> 수인한도 분석 격자를 생성합니다.
>
> 입력 변수값을 통해 격자를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type    | Description                     |
| --------- | ------- | ------------------------------- |
| layerName | string  | 격자 객체를 관리할 레이어 명칭. |
| gap       | number  | 격자의 가로 세로 크기.          |
| isClip    | boolean | 균등 분활 격자 생성 유무 설정.  |

-   Return

    -   true : 생성 성공.
    -   false : 생성 실패.
    -   실패 조건
        -   입력 된 레이어 명칭이 지도에 생성되지 않는 경우.
        -   격자 영역 생성 시 입력된 점이 3개 이하인 경우.

-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Grid Shadow](https://sandbox.egiscloud.com/code/main.do?id=analysis_grid_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript
var gridShadow = Module.getAnalysisGridShadow();
gridShadow.create("gridlayer", 10, true);
```

{% endtab %}
{% endtabs %}

### getResult() → string

> 수인한도 분석 결과를 반환합니다.
>
> 격자 별 일조량 분석 결과를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   각 격자별 일조량, 연속 일조량 결과 반환 (Json).
-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Grid Shadow](https://sandbox.egiscloud.com/code/main.do?id=analysis_grid_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript
var gridShadow = Module.getAnalysisGridShadow();
var result = gridShadow.getResult();
const json = JSON.parse(result);
```

{% endtab %}
{% endtabs %}

### reset() → boolean

> 수인한도 분석 격자 옵션을 초기화 합니다.
>
> 격자별 분석 유무, 색상과 같은 옵션을 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return

    -   true : 초기화 성공.
    -   false : 초기화 실패.
    -   실패 조건
        -   생성 격자가 없는 경우.
        -   수인한도 분석에 사용할 레이어가 없는 경우.

-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Grid Shadow](https://sandbox.egiscloud.com/code/main.do?id=analysis_grid_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript
var gridShadow = Module.getAnalysisGridShadow();
gridShadow.reset();
```

{% endtab %}
{% endtabs %}

### setAnalysis(id, isAnalysis) → boolean

> 격자별 분석 유무를 설정합니다.
>
> 입력 id 변수값을 통해 수인한도 분석 유무 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type    | Description                                                    |
| ---------- | ------- | -------------------------------------------------------------- |
| id         | string  | 격자 별 고유 명칭.                                             |
| isAnalysis | boolean | <p>true: 수인한도 분석 포함.<br>false: 수인한도 분석 제외.</p> |

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
    -   실패 조건
        -   생성 격자가 없는 경우.
        -   수인한도 분석에 사용할 레이어가 없는 경우.
-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Grid Shadow](https://sandbox.egiscloud.com/code/main.do?id=analysis_grid_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript
var gridShadow = Module.getAnalysisGridShadow();
gridShadow.setAnalysis("id", false);
```

{% endtab %}
{% endtabs %}

### prograss(object) → string

> 분석 진행률을 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name       | Type    	 | Description                                                    |
| ---------- | --------- | -------------------------------------------------------------- |
| object     | function  | 분석 진행률을 반환받을 callback을 설정합니다.                       |

-   Return
    -   success : 설정 성공.
    -   실패 조건
        -   callback function을 설정하지 않을 경우.
-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Grid Shadow](https://sandbox.egiscloud.com/code/main.do?id=analysis_grid_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setColor(id, color) → boolean

> 격자별 분석 색상을 설정합니다.
>
> 입력 id 변수값을 통해 수인한도 분석 색상을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type                          | Description        |
| ----- | ----------------------------- | ------------------ |
| id    | string                        | 격자 별 고유 명칭. |
| color | [JSColor](../core/jscolor.md) | 격자 별 변경 색상. |

-   Return

    -   true : 설정 성공.
    -   false : 설정 실패.
    -   실패 조건
        -   생성 격자가 없는 경우.
        -   수인한도 분석에 사용할 레이어가 없는 경우.

-   Sample
    -   Refer to function setEarthquakeMesh.
    -   [Sandbox_Grid Shadow](https://sandbox.egiscloud.com/code/main.do?id=analysis_grid_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript
var gridShadow = Module.getAnalysisGridShadow();
gridShadow.setColor("id", new Module.JSColor(150, 0, 255, 0));
```

{% endtab %}
{% endtabs %}

### startAnalysis(startTime, endTime, interval) → boolean

> 수인한도 분석을 실행합니다.
>
> 수인한도 분석에 필요한 시간 정보를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type                                | Description                            |
| --------- | ----------------------------------- | -------------------------------------- |
| startTime | [JSDateTime](../core/jsdatetime.md) | 분석 시작 시간.                        |
| endTime   | [JSDateTime](../core/jsdatetime.md) | 분석 종료 시간.                        |
| interval  | number                              | 수인한도 분석 진행 간격 설정 (분 단위) |

-   Return

    -   true : 분석 성공.
    -   false : 분석 실패.
    -   실패 조건
        -   생성 격자가 없는 경우.
        -   수인한도 분석에 사용할 레이어가 없는 경우.
        -   수인한도 분석에 필요한 선택된 시설물이 없는 경우.

-   Sample
    -   function setEarthquakeMesh 참조.
    -   [Sandbox_Grid Shadow](https://sandbox.egiscloud.com/code/main.do?id=analysis_grid_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript
var gridShadow = Module.getAnalysisGridShadow();
gridShadow.startAnalysis(new Module.JSDateTime(2023, 4, 17, 9, 30, 0), new Module.JSDateTime(2023, 4, 17, 15, 30, 0), 10);
```

{% endtab %}
{% endtabs %}

### createWindow(layerName) → boolean

> 일조량 분석을 위한 창문 객체를 생성합니다.
>
> 마우스 클릭 이벤트(Module.MML_ANALYS_WINDOWSHADOW)를 통해 입력점 2개로 창문을 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name      | Type   | Description                    |
| --------- | ------ | ------------------------------ |
| layerName | string | 창문 객체를 관리할 레이어 명칭 |

-   Return

    -   true : 생성 성공.
    -   false : 생성 실패.
    -   실패 조건
        -   일조량 분석을 사용할 레이어가 없는 경우.
        -   창문 생성 시 입력된 점이 2개가 아닌 경우.

-   Sample
    -   function inputWindow 참조.
    -   [Sandbox_Window Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_window_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### copyPasteWindow() → boolean

> 생성된 창문을 복사 후 붙여넣기 합니다.
>
> 가장 최근에 생성한 창문을 복사합니다.
>
> 마우스 클릭 이벤트(Module.MML_ANALYS_WINDOWSHADOW)를 통해 입력된 좌표를 창문의 좌상단으로 복사합니다.

{% tabs %}
{% tab title="Information" %}

-   Return

    -   true : 복사 성공.
    -   false : 복사 실패.
    -   실패 조건
        -   일조량 분석을 사용할 레이어가 없는 경우.
        -   생성된 창문이 없는 경우.
        -   마우스 클릭 이벤트를 통해 입력된 점이 없는 경우.

-   Sample
    -   function copyPasteWindow 참조.
    -   [Sandbox_Window Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_window_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### copyPasteFloor() → boolean

> 생성된 한 층에 존재하는 모든 창문을 다른층으로 복사후 붙여넣기 합니다.
>
> 가장 최근에 생성한 한 층에 존재하는 모든 창문을 복사합니다.
>
> 마우스 클릭 이벤트(Module.MML_ANALYS_WINDOWSHADOW)를 통해 입력된 좌표를 창문의 좌상단으로 복사합니다.

{% tabs %}
{% tab title="Information" %}

-   Return

    -   true : 복사 성공.
    -   false : 복사 실패.
    -   실패 조건
        -   일조량 분석을 사용할 레이어가 없는 경우.
        -   생성된 창문이 없는 경우.
        -   마우스 클릭 이벤트를 통해 입력된 점이 없는 경우.

-   Sample
    -   function copyPasteFloor 참조.
    -   [Sandbox_Window Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_window_shadow)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}