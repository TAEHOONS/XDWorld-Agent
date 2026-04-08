---
description: 지도 내 분석 기능 설정을 위한 API입니다.
---

# JSAnalysis

> Module.getAnalysis API를 생성합니다.

```javascript
var analysis = Module.getAnalysis();
```

## Function

### createShadow(year, month, day, hour, minute) → boolean

> 설정한 날짜, 시간을 기준으로 건물에 대한 그림자를 생성합니다.

{% tabs %}
{% tab title="Name" %}

| Name   | Type   | Description |
| :----- | :----- | :---------- |
| year   | number | 년도.       |
| month  | number | 월.         |
| day    | number | 일.         |
| hour   | number | 시간.       |
| minute | number | 분.         |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getAnalysis.createShadow(2018, 5, 28, 15, 0);
```

{% endtab %}
{% endtabs %}

### createSlopePlane(angle, color) → boolean

> 시곡면 분석 삼각형 평면을 생성합니다.

{% tabs %}
{% tab title="Name" %}

| Name  | Type                          | Description    |
| :---- | :---------------------------- | :------------- |
| angle | number                        | 지형과의 각도. |
| color | [JSColor](../core/jscolor.md) | 평면 색상.     |

-   Return
    -   true: 생성 성공.
    -   false: 생성 실패.
-   Sample
    -   function getSlopePlane 참조.
    -   [Sandbox_Slope Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_building_height_regulation)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### CreateInterpolationPath(option) → array

> 보간된 선을 구성하는 좌표 목록을 반환합니다.

{% tabs %}
{% tab title="Name" %}

| Name   | Type                                                                           | Description |
| :----- | :----------------------------------------------------------------------------- | :---------- |
| option | [JSAnalysis.InterpolationOption](jsanalysis.md#jsanalysis.interpolationoption) | 속성 정보.  |

-   Return
    -   array: 보간된 선 좌표 목록 반환 성공.
    -   NULL: 보간된 라인 좌표 모곩 반환 실패.
-   Sample
    -   function createInterpolatedLine 참조.
    -   [Sandbox_Line Interpolation (Curved)](https://sandbox.egiscloud.com/code/main.do?id=object_line_interpolate_curved)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getGridAnal() → [JSGridAnal](../analysis/jsgridanal.md)

> JSGridAnal 클래스를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   [JSGridAnal](../analysis/jsgridanal.md): 반환 성공.
    -   null : 반환 실패.
-   Sample
    -   function setWindRenderMode 참조.
    -   [Sandbox_Wind Representation](https://sandbox.egiscloud.com/code/main.do?id=effect_wind)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getJomangRatio(height) → string

> 조망 차폐율을 반환합니다.
>
> 입력 변수값이 설정한 높이 이하 인 지형 고도 값을 가진 영역은 지형, 이상은 산으로 판단합니다.

{% tabs %}
{% tab title="Name" %}

| Name   | Type   | Description                      |
| :----- | :----- | :------------------------------- |
| height | number | 지형, 산 기준 높이 (meter 단위). |

-   Return

    -   다음 순서로 문자열이 구성 (건물#차폐율#산#차폐율#지형#차폐율#하늘#차폐율)

-   Sample
    -   function getJomangRatio 참조.
    -   [Sandbox_View Ratio](https://sandbox.egiscloud.com/code/main.do?id=camera_jomang_ratio)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getJudong(angle) → string

> 지동 길이를 측정하고 측정 정보를 반환합니다.
>
> 입력 변수값은 측정의 기준 퍼짐각도 입니다.

{% tabs %}
{% tab title="Name" %}

| Name  | Type   | Description |
| :---- | :----- | :---------- |
| angle | number | 퍼짐각      |

-   Return

    -   다음 순서로 문자열이 구성 (레이어명#객체키#주동길이#경도#위도)

-   Sample
    -   function getJudong 참조.
    -   [Sandbox_Main Building Length Analysis](https://sandbox.egiscloud.com/code/main.do?id=analysis_building_width)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setAllObjectRenderShadow(type)

> 가시화 된 시설물에 대한 그림자 생성 유무를 설정합니다.

{% tabs %}
{% tab title="Name" %}

| Name | Type    | Description                                                                        |
| :--- | :------ | :--------------------------------------------------------------------------------- |
| type | boolean | <p>true: 모든 시설물 그림자 객체 생성.<br>false: 선택 시설물 그림자 객체 생성.</p> |

-   Sample
    -   function initPage 참조.
    -   [Sandbox_Shadow](https://sandbox.egiscloud.com/code/main.do?id=effect_shadow_play)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setShadowSimulation(type)

> 그림자 시뮬레이션 실행, 종료를 설정합니다.

{% tabs %}
{% tab title="Name" %}

| Name | Type    | Description                                                            |
| :--- | :------ | :--------------------------------------------------------------------- |
| type | boolean | <p>true: 그림자 시뮬레이션 실행.<br>false: 그림자 시뮬레이션 종료.</p> |

-   Sample
    -   function executeShadowSimulation 참조.
    -   [Sandbox_Shadow](https://sandbox.egiscloud.com/code/main.do?id=effect_shadow_play)

{% endtab %}
{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setShadowSimulTerm(term)

> 그림자 시뮬레이션 진행 시간 간격을 설정합니다.

{% tabs %}
{% tab title="Name" %}

| Name | Type   | Description                                 |
| :--- | :----- | :------------------------------------------ |
| term | number | 그림자 시뮬레이션 진행 간격 설정 (분 단위). |

-   Sample
    -   function setShadowSimulationTimeTerm 참조.
    -   [Sandbox_Shadow](https://sandbox.egiscloud.com/code/main.do?id=effect_shadow_play)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getAnalysis.setShadowSimulTerm(30);
```

{% endtab %}
{% endtabs %}

### setShadowSimulTime(year, month, day, startHour, startMin, endHour, endMin)

> 그림자 시뮬레이션에 필요한 시간 정보를 설정합니다.

{% tabs %}
{% tab title="Name" %}

| Name      | Type   | Description           |
| :-------- | :----- | :-------------------- |
| year      | number | 시뮬레이션 년도.      |
| month     | number | 시뮬레이션 월.        |
| day       | number | 시뮬레이션 일.        |
| startHour | number | 시뮬레이션 시작 시간. |
| startMin  | number | 시뮬레이션 시작 분.   |
| endHour   | number | 시뮬레이션 종료 시간. |
| endMin    | number | 시뮬레이션 종료 분.   |

-   Sample
    -   function setShadowSimulationTimeTerm 참조.
    -   [Sandbox_Shadow](https://sandbox.egiscloud.com/code/main.do?id=effect_shadow_play)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getAnalysis.setShadowSimulTime(2018, 05, 28, 9, 0, 14, 30);
```

{% endtab %}
{% endtabs %}

### setViewshedMode(apply)

> 가시권 분석을 실행, 종료를 설정합니다.

{% tabs %}
{% tab title="Name" %}

| Name  | Type    | Description                                                |
| :---- | :------ | :--------------------------------------------------------- |
| apply | boolean | <p>true: 가시권 분석 실행.<br>false: 가시권 분석 종료.</p> |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### setShadowDrawMode(mode)

> 그림자 종류를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    | Description                                                |
| ----  | ------  | ---------------------------------------------------------- |
| mode  | number  | <p>0: 선택되지 않은 건물의 그림자영역 제외하고 가시화.<br>1: 선택된 건물의 그림자 가시화.<br>2: 그림자 가시화 중지.<br>3: 그림자를 선으로 가시화.<br>4: 그림자를 면으로 가시화.</p> 										|

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### CreateShadowOutLine(time, color) → boolean

> 그림자 종류를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    							   | Description                    |
| ----  | -----------------------------------  | ------------------------------ |
| time  | [JSDateTime](../core/jsdatetime.md)  | 그림자 생성할 시간.			    |
| color | [JSColor](../core/jscolor.md)  	   | 그림자 색상.			   			|

-   Return
    -   true : 설정 성공.
    -   false : 설정 실패.
    -   실패 조건
        -   엔진 로드에 실패했을 경우.

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### SetRenderTerrainShadow(option)

> 지형 그림자 생성여부를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    	| Description                    |
| ----  | --------  | ------------------------------ |
| option | boolean  | 지형 그림자 생성 여부.		     |

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### clearShadow()

> 그림자를 초기화 합니다.

{% tabs %}
{% tab title="Information" %}

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### checkInsideArea(array, object, type) → boolean

> 입력된 영역과 객체의 포함여부를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    								  | Description                    					 		|
| ----  | --------------------------------------  | ------------------------------------------------------- |
| array | [JSVec3Array](../core/jsvec3array.md)   | 비교할 영역 좌표 배열.		    					 		|
| object | [JSObject](../object/jsobject.md)  	  | 비교할 객체.		    							 		|
| type   | number  								  | <p>0: 완전 포함될 경우.<br>1: 일부라도 포함될 경우.</p>	  	|

-   Return
    -   true : 설정 성공.
    -   false : 설정 조건에 맞는 객체가 없을 경우.
		
{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### checkInsideAreas(array, parts, object, type) → boolean

> 여러개의 입력된 영역과 객체의 포함여부를 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name  | Type    								  | Description                    					 		|
| ----  | --------------------------------------  | ------------------------------------------------------- |
| array | [JSVec3Array](../core/jsvec3array.md)   | 비교할 영역 좌표 배열.		    					 		|
| parts | [JSCollection](../core/collection.md)   | 비교할 영역 parts.		    							|
| object | [JSObject](../object/jsobject.md)  	  | 비교할 객체.		    							 		|
| type   | number  								  | <p>0: 완전 포함될 경우.<br>1: 일부라도 포함될 경우.</p>	  	|

-   Sample
    -   function setShadowSimulationTimeTerm 참조.
    -   [Sandbox_Object Inside Area](https://sandbox.egiscloud.com/code/main.do?id=analysis_object_inside_area)

{% endtab %}

{% tab title="Template" %}

```javascript

```

{% endtab %}
{% endtabs %}

### getSunset(year, month, day) → number

> 입력한 날짜를 기준으로 일몰 시간(시각)을 반환합니다.  

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description |
| ------ | ------ | ----------- |
| year   | number | 년도        |
| month  | number | 월 (1~12)   |
| day    | number | 일 (1~31)   |

- Return  
  - number: 일몰 시간
  - 0.0: 계산 실패 (지도 미로드 등)

{% endtab %}
{% tab title="Template" %}

```javascript
const sunsetTime = Module.getAnalysis().getSunset(2025, 4, 2);
console.log("Sunset:", sunsetTime);
```

{% endtab %}
{% endtabs %}

### getSunrise(year, month, day) → number

> 입력한 날짜를 기준으로 일출 시간(시각)을 반환합니다.  
> 반환된 값은 24시간제 기준의 실수형 시간값입니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type   | Description |
| ------ | ------ | ----------- |
| year   | number | 년도        |
| month  | number | 월 (1~12)   |
| day    | number | 일 (1~31)   |

- Return  
  - number: 일출 시간
  - 0.0: 계산 실패 (지도 미로드 등)

{% endtab %}
{% tab title="Template" %}

```javascript
const sunriseTime = Module.getAnalysis().getSunrise(2025, 4, 2);
console.log("Sunrise:", sunriseTime);
```

{% endtab %}
{% endtabs %}

### setShadowMapSize(size)

> 그림자 맵 해상도를 설정합니다.  

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description                      |
| ---- | ------ | -------------------------------- |
| size | number | 그림자 맵 해상도 (픽셀 단위) 입력 |

- Return  
  - 없음 (void)
 
> 너무 큰 해상도를 설정할 경우 성능 저하가 발생할 수 있습니다.

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getAnalysis().setShadowMapSize(2048);
```

{% endtab %}
{% endtabs %}

### setLimitSunAngle(enable, angle)

> 태양 고도 각도 제한 여부와 제한 각도를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name   | Type    | Description                                  |
| ------ | ------- | -------------------------------------------- |
| enable | boolean | <p>true: 제한 활성화<br>false: 제한 비활성화</p> |
| angle  | number  | 제한할 최소 태양 고도 각도 (degree 단위)      |

- Return  
  - 없음 (void)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getAnalysis().setLimitSunAngle(true, 5.0);
```

{% endtab %}
{% endtabs %}

### setSunshineObject(objectNames)

> 일조량 분석 시 분석 대상 객체들을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name        | Type   | Description                                  |
| ----------- | ------ | -------------------------------------------- |
| objectNames | string | 분석 대상 객체들의 키 값 |

-   Return  
    -   없음 (void)

{% endtab %}
{% tab title="Template" %}

```javascript
Module.getAnalysis().setSunshineObject("Building01,Building02");
```

{% endtab %}
{% endtabs %}

### CalculateSunshineJson(options) → array

> 지정된 지점들의 일조 시간을 분석하여 각 지점의 일조 시간을 분 단위로 반환합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type   | Description                                      |
| ------- | ------ | ------------------------------------------------ |
| options | object | 일조 분석 옵션 객체.                             |

**options 필드 설명**:

| Field         | Type     | Required | Default         | Description                                                      |
| ------------- | -------- | -------- | --------------- | ---------------------------------------------------------------- |
| positions     | array    | ✅       |                 | 분석할 지점 목록. `[longitude, latitude, altitude]` 형식 배열. |
| timerange     | object   | ❌       | 오늘 5시~20시   | 시뮬레이션 시간 정보. year, month, day, starthour, endhour 등 포함. |
| interval      | number   | ❌       | 20              | 분석 시간 간격(단위: 분).                                       |
| analysistype  | number   | ❌       | 1               | 분석 대상 타입. `0`: 선택 객체, `1`: 가시 객체.                |
| skip          | number   | ❌       | 0               | 분석 생략할 객체 개수.                                           |

- Return:
    - array: 각 지점별 일조 시간(분) 리스트.
    - null: 분석 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
const options = {
  positions: [
    [127.0, 37.5, 20],
    [127.01, 37.51, 25]
  ],
  timerange: {
    year: 2025,
    mounth: 4,
    day: 2,
    starthour: 6,
    startminute: 0,
    startsecond: 0,
    endhour: 18,
    endminute: 0,
    endsecond: 0
  },
  interval: 10,
  analysistype: 1
};

const sunshine = Module.getAnalysis().CalculateSunshineJson(options);
console.log(sunshine); // [520, 430] 분 단위 일조량
```

{% endtab %}
{% endtabs %}



### Type Definitions

#### JSAnalysis.InterpolationOption

> Interpolation line coordinate creation options.

| Name        | Type                                                          | Description            |
| ----------- | ------------------------------------------------------------- | ---------------------- |
| positions   | array([JSVector2D](../core/jsvector2d.md))                    | 보간 선 시작점 목록.   |
| input       | array([Interpolation](../etc/tag-list.md#interpolation-type)) | 보간 계산 입력점 목록. |
| rect        | [Rect2D](../etc/tag-list.md#rect2d-style-type)                | 선 생성 영역.          |
| vertexcount | number                                                        | 선 형상 정점 수.       |
| scale       | number                                                        | 선 생성 간격.          |
